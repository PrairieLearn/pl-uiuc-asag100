import warnings
import html, itertools, nltk, pickle, re
import numpy as np
from unidecode import unidecode
from nltk.corpus import stopwords
from spellchecker import SpellChecker
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *

def unescape_response(response):
    response = unidecode(response)
    prev_response = response
    response = html.unescape(response)
    while prev_response != response:
        prev_response = response
        response = html.unescape(response)

    return response

def tokenize(response, nltk_data_path, token_format='none'):
    if nltk_data_path not in nltk.data.path:
        nltk.data.path.append(nltk_data_path)
    
    spell_checker = SpellChecker()
    spell_checker.distance = 1
    
    punctuations = ' ,.:;?'
    preprocessed_response = []
    for i in range(len(response)):
        if response[i] in ["'", '"']:
            if i != 0 and i != len(response) - 1:
                if response[i - 1] not in punctuations and response[i + 1] not in punctuations:
                    preprocessed_response.append(response[i])
        else:
            preprocessed_response.append(response[i])
    response = ''.join(preprocessed_response)

    operators = '+-*/%=<>()[]{}#'
    preprocessed_response = []
    for i in range(len(response)):
        if response[i] in operators:
            if i != 0 and response[i - 1] != ' ':
                preprocessed_response.append(' ')
            preprocessed_response.append(response[i])
            if i != len(response) - 1 and response[i + 1] != ' ':
                preprocessed_response.append(' ')
        else:
            preprocessed_response.append(response[i])

    response = ''.join(preprocessed_response)

    spell_checker_skip = ["it's"]
    tokens_list = []
    for sentence in nltk.sent_tokenize(response):
        nltk_tokens = nltk.word_tokenize(sentence)
        tokens = []
        i = 0
        while i < len(nltk_tokens):
            if i < len(nltk_tokens) - 1 and nltk_tokens[i + 1][0] == "'":
                tokens.append(nltk_tokens[i].lower() + nltk_tokens[i + 1].lower())
                i += 1
            elif nltk_tokens[i] not in punctuations:
                tokens.append(nltk_tokens[i].lower())
            i += 1

        if token_format == "lemma":
            lemmatizer = WordNetLemmatizer()
            tokens_list.append([lemmatizer.lemmatize(spell_checker.correction(token)) if token not in spell_checker_skip
                                else lemmatizer.lemmatize(token) for token in tokens])
        elif token_format == "stem":
            stemmer = PorterStemmer()
            tokens_list.append([stemmer.stem(spell_checker.correction(token)) if token not in spell_checker_skip
                                else stemmer.stem(token) for token in tokens])
        else:
            tokens_list.append([spell_checker.correction(token) if token not in spell_checker_skip
                                else token for token in tokens])

    return tokens_list

def bowize(token_to_index, tokens_list):
    tokens = set(itertools.chain.from_iterable(tokens_list))
    
    X = np.zeros((1, len(token_to_index)))
    for token in tokens:
        if token in token_to_index:
            X[0, token_to_index[token]] = 1
    
    return X
    
def bigramize(to_index_tuple, tokens_list):
    token_to_index, bigram_to_index = to_index_tuple
    
    X = np.zeros((1, len(token_to_index) + len(bigram_to_index)))
    
    tokens = set(itertools.chain.from_iterable(tokens_list))
    for token in tokens:
        if token in token_to_index:
            X[0, token_to_index[token]] = 1
    
    for tokens in tokens_list:
        for bigram in map(lambda x : x[0] + ' ' + x[1], zip(tokens[0:-1], tokens[1:])):
            if bigram in bigram_to_index:
                X[0, len(token_to_index) + bigram_to_index[bigram]] = 1
    
    return X

def trigramize(to_index_tuple, tokens_list):
    token_to_index, bigram_to_index, trigram_to_index = to_index_tuple
    
    X = np.zeros((1, len(token_to_index) + len(bigram_to_index) + len(trigram_to_index)))
    
    tokens = set(itertools.chain.from_iterable(tokens_list))
    for token in tokens:
        if token in token_to_index:
            X[0, token_to_index[token]] = 1
    
    for tokens in tokens_list:
        for bigram in map(lambda x : x[0] + ' ' + x[1], zip(tokens[0:-1], tokens[1:])):
            if bigram in bigram_to_index:
                X[0, len(token_to_index) + bigram_to_index[bigram]] = 1
                
    for tokens in tokens_list:
        for trigram in map(lambda x : x[0] + ' ' + x[1] + ' ' + x[2], zip(tokens[0:-2], tokens[1:-1], tokens[2:])):
            if trigram in trigram_to_index:
                X[0, len(token_to_index) + len(bigram_to_index) + trigram_to_index[trigram]] = 1
    
    return X

def nlp_detect_garbage(tokens_list, vocab_path):
    vocabulary = pickle.load(open(vocab_path, 'rb'))

    count = 0
    total = 0
    for tokens in tokens_list:
        for token in tokens:
            if token in vocabulary:
                count += 1
            total += 1

    if total <= 2:
        return True
    return 1. * count / total < 0.6

def nlp_grade_response(nltk_data_path, model_path, response, threshold=0.5):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        _, _, nlp_train_config, _, feature_map, feature_size, model = pickle.load(open(model_path, 'rb'))

    token_format = nlp_train_config['model_config']['token_format'] if 'token_format' in nlp_train_config['model_config'] else 'none'

    tokens_list = tokenize(unescape_response(response), nltk_data_path, token_format)

    feature_set = nlp_train_config['model_config']['feature_set']
    if feature_set == 'bow':
        featurize = bowize
    elif feature_set == 'bigram':
        featurize = bigramize
    elif feature_set == 'trigram':
        featurize = trigramize
    else:
        raise Exception(f'Unrecognized feature_set: {featuer_set}')

    X = np.zeros((1, feature_size))
    X[0, :] = featurize(feature_map, tokens_list)
    
    return 1 if model.predict_proba(X)[0][1] > threshold else 0
