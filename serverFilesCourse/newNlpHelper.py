import torch

'''
separate sentence into characters and subwords using tokenizer
combine tokens using math and latex grammar
convert to input ids and attention mask
'''
def generateTokens(tokenizer, sentences):
    
    input_ids = []
    for proof in sentences:
        
        tokens = tokenizer.tokenize(proof)
        combined_tokens = ['[CLS]']
        
        combine_amount = 0
        for i in range(len(tokens)):
            
            word = tokens[i]
            if word[: 2] == '##':
                combined_tokens[-1] += word[2: ]
                if combined_tokens[-1] in ['frac', 'mathbb', 'forall', 'geq', 'leq']:
                    combined_tokens.pop(-1)
                    combined_tokens.pop(-1)
                elif combined_tokens[-1][: 4] == 'cdot':
                    combined_tokens[-1] = '*'
                    combined_tokens.pop(-2)
                continue
            
            if word in ['$', '#', '{', '}']:
                continue
            
            if word in ['in'] and len(combined_tokens):
                combined_tokens[-1] = word
                continue
            
            if i != 0 and word == '(':
                combine_amount = 10
                
            if combine_amount:
                combined_tokens[-1] += word
                if tokens[i] == ')':
                    combine_amount = 0
                else:
                    combine_amount -= 1
            else:
                combined_tokens.append(word)

        combined_tokens.append('[SEP]')
        while len(combined_tokens) > 512:
            combined_tokens.pop(-1)
        combined_tokens = tokenizer.convert_tokens_to_ids(combined_tokens)
        while len(combined_tokens) < 512:
            combined_tokens.append(0)
        input_ids.append(combined_tokens)
                
    input_ids = torch.tensor(input_ids)
    attention_mask = (input_ids != 0)
    return input_ids, attention_mask.long()