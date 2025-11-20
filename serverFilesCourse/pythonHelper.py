import random

def fractionOfTime(percent):
    return random.random() < percent

# Random integer between -100 and 100 (inclusive)
def randomInt():
    return str(random.randint(-100, 100))

# Random float between -100.99 and 100.99 (inclusive)
def randomFloat():
    value = random.randint(-100, 100)    
    return str(value) + '.' + str(random.randint(0, 99))

# Randomly generate an int or a float (based on the above)
def randomNumber(percentage = 0.5):
    return randomInt() if fractionOfTime(percentage) else randomFloat()

def randomQuote():
    return '"' if fractionOfTime(0.5) else "'"

def enquote(thing):
    quote = randomQuote()
    return quote + str(thing) + quote

# Random string containing a number
def randomNumberString():
    return enquote(randomNumber())

def stringContentsSameIndependentOfQuoteTypes(submitted, correct):
    quotes = ['"', "'"]
    if len(submitted) == 0:
        return False
    if submitted[0] not in quotes:
        return False
    if submitted[0] != submitted[-1]:
        return False
    if submitted[1:-1] != correct[1:-1]:
        return False
    return True

# Random string containing characters
def randomString(baselength = 0):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    random.shuffle(letters)
    quote = '"' if fractionOfTime(0.5) else "'"
    return quote + "".join(letters[:random.randint(baselength+1, baselength+7)]) + quote

startingVarNameCharacters = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ_'               # no l or O
invalidStartingVarNameCharacters = '0123456789`~!@#$%^&*'
validVarNameCharacters = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ_0123456789'        # no l or O
invalidVarNameCharacters = '`~!@#$%^&'

def xl_get_column(col):
    first_index  = (col - 1) // 26
    name = '' if first_index == 0 else chr(ord('A') + first_index - 1)
    second_index = (col - 1) % 26
    return name + chr(ord('A') + second_index)

def xl_get_cell_name(col, row):
    return xl_get_column(col) + str(row)                      

def xl_copy_into_sheet(sheet, col, row, values, orientation='col', write_zeroes=True):
    for i in range(len(values)):
        for j in range(len(values[i])):
            if (not write_zeroes) and values[i][j] == 0:
                continue
            if orientation == 'col':
                sheet[xl_get_cell_name(col + i, row + j)] = values[i][j]
            else:
                sheet[xl_get_cell_name(col + j, row + i)] = values[i][j]

def randomVarName():
    str = ""
    for i in range(random.randint(5,12)):
        str += random.choice(validVarNameCharacters)
    return random.choice(startingVarNameCharacters) + str

def randomVarNameInvalidStart():
    return random.choice(invalidStartingVarNameCharacters) + randomVarName()

def randomVarNameInvalidMiddle():
    str = randomVarName()
    index = random.randint(1, len(str) - 1)
    return str[:index] + random.choice(invalidVarNameCharacters) + str[index:]

def randomWord():
    return random.choice(['apple', 'banana', 'orange', 'grape'])


def randomInteger(k = 1):
    selection = random.choices(list(range(1, 1000)), k=k)
    return selection[0] if k == 1 else selection
    
def randomFloatPoint(k = 1):
    if k == 1:
        return random.uniform(0, 100)
    return [random.uniform(0, 100) for i in range(k)]

def randomFruit(k = 1):
    fruits = ["Apple", "Akee", "Apricot", "Avocado", "Banana", "Bilberry", "Blackberry", "Blackcurrant", "Blueberry", "Boysenberry", "Currant", "Cherry", "Cloudberry", "Coconut", "Cranberry", "Cucumber", "Damson", "Date", "Durian", "Elderberry", "Feijoa", "Fig", "Gooseberry", "Grape", "Raisin", "Grapefruit", "Guava", "Honeyberry", "Huckleberry", "Jabuticaba", "Jackfruit", "Jambul", "Jostaberry", "Jujube", "Kiwifruit", "Kumquat", "Lemon", "Lime", "Loquat", "Longan", "Lychee", "Mango", "Mangosteen", "Marionberry", "Melon", "Cantaloupe", "Honeydew", "Watermelon", "Mulberry", "Nectarine", "Nance", "Orange", "Clementine", "Mandarine", "Tangerine", "Papaya", "Passionfruit", "Peach", "Pear", "Persimmon", "Plantain", "Plum", "Pineapple", "Pineberry", "Pomegranate", "Pomelo", "Quince", "Raspberry", "Salmonberry", "Redcurrant", "Salak", "Satsuma", "Soursop", "Strawberry", "Tamarillo", "Tamarind", "Yuzu"]
    selection = random.sample(fruits, k)
    return selection[0] if k == 1 else selection

def randomAnimal(k = 1):
    animals = ['aardvark', 'alligator', 'crocodile', 'alpaca', 'ant', 'antelope', 'ape', 'armadillo', 'donkey', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'bee', 'beetle', 'buffalo', 'butterfly', 'camel', 'carabao', 'caribou', 'cat', 'cattle', 'cheetah', 'chimpanzee', 'chinchilla', 'cicada', 'clam', 'cockroach', 'cod', 'coyote', 'crab', 'cricket', 'crow', 'raven', 'deer', 'dinosaur', 'dog', 'dolphin', 'porpoise', 'duck', 'eagle', 'echidna', 'eel', 'elephant', 'elk', 'ferret', 'fish', 'fly', 'fox', 'frog', 'toad', 'gerbil', 'giraffe', 'gnat', 'wildebeest', 'goat', 'goldfish', 'goose', 'gorilla', 'grasshopper', 'hamster', 'hare', 'hedgehog', 'herring', 'hippopotamus', 'hornet', 'horse', 'hound', 'hyena', 'impala', 'insect', 'jackal', 'jellyfish', 'kangaroo', 'wallaby', 'koala', 'leopard', 'lion', 'lizard', 'llama', 'locust', 'louse', 'macaw', 'mallard', 'mammoth', 'manatee', 'marten', 'mink', 'minnow', 'mole', 'monkey', 'moose', 'mosquito', 'mouse', 'rat', 'mule', 'muskrat', 'otter', 'ox', 'oyster', 'panda', 'pig', 'hog', 'platypus', 'porcupine', 'pug', 'rabbit', 'raccoon', 'reindeer', 'rhinoceros', 'salmon', 'sardine', 'scorpion', 'seal', 'serval', 'shark', 'sheep', 'skunk', 'snail', 'snake', 'spider', 'squirrel', 'swan', 'termite', 'tiger', 'trout', 'turtle', 'tortoise', 'walrus', 'wasp', 'weasel', 'whale', 'wolf', 'wombat', 'woodchuck', 'worm', 'yak', 'yellowjacket', 'zebra']
    selection = random.sample(animals, k)
    return selection[0] if k == 1 else selection

def randomState(k = 1):
    states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
    if k == 1:
        return random.choice(states)
    return random.sample(states, k)

def randomCities(k = 1):
    cities = [
('Chicago', 'City', '2695598', 'Cook'),
('Aurora', 'City', '197899', 'Kane'),
('Rockford', 'City', '152871', 'Winnebago'),
('Joliet', 'City', '147433', 'Will'),
('Naperville', 'City', '141853', 'DuPage'),
('Springfield', 'City', '116250', 'Sangamon'),
('Peoria', 'City', '115007', 'Peoria'),
('Elgin', 'City', '108188', 'Kane'),
('Waukegan', 'City', '89078', 'Lake'),
('Cicero', 'Town', '83891', 'Cook'),
('Champaign', 'City', '81055', 'Champaign'),
('Bloomington', 'City', '76610', 'McLean'),
('Decatur', 'City', '76122', 'Macon'),
('Arlington Heights', 'Village', '75101', 'Cook'),
('Evanston', 'City', '74486', 'Cook'),
('Schaumburg', 'Village', '74227', 'Cook'),
('Bolingbrook', 'Village', '73366', 'Will'),
('Palatine', 'Village', '68557', 'Cook'),
('Skokie', 'Village', '64784', 'Cook'),
('Des Plaines', 'City', '58364', 'Cook'),
('Orland Park', 'Village', '56767', 'Cook'),
('Tinley Park', 'Village', '56703', 'Cook'),
('Oak Lawn', 'Village', '56690', 'Cook'),
('Berwyn', 'City', '56657', 'Cook'),
('Mount Prospect', 'Village', '54167', 'Cook'),
('Wheaton', 'City', '52894', 'DuPage'),
('Normal', 'Town', '52497', 'McLean'),
('Hoffman Estates', 'Village', '51895', 'Cook'),
('Oak Park', 'Village', '51878', 'Cook'),
('Downers Grove', 'Village', '47833', 'DuPage'),
('Glenview', 'Village', '44692', 'Cook'),
('Belleville', 'City', '44478', 'St. Clair'),
('Elmhurst', 'City', '44121', 'DuPage'),
('DeKalb', 'City', '43862', 'DeKalb'),
('Moline', 'City', '43483', 'Rock Island'),
('Lombard', 'Village', '43395', 'DuPage'),
('Buffalo Grove', 'Village', '41496', 'Lake'),
('Urbana', 'City', '41250', 'Champaign'),
('Bartlett', 'Village', '41208', 'Cook'),
('Crystal Lake', 'City', '40743', 'McHenry'),
('Quincy', 'City', '40633', 'Adams'),
('Hanover Park', 'Village', '39973', 'Cook'),
('Streamwood', 'Village', '39858', 'Cook'),
('Carol Stream', 'Village', '39711', 'DuPage'),
('Romeoville', 'Village', '39680', 'Will'),
('Plainfield', 'Village', '39581', 'Will'),
('Rock Island', 'City', '39018', 'Rock Island'),
('Carpentersville', 'Village', '37691', 'Kane'),
('Wheeling', 'Village', '37648', 'Cook'),
('Park Ridge', 'City', '37480', 'Cook'),
('Calumet City', 'City', '37042', 'Cook'),
('Addison', 'Village', '36942', 'DuPage'),
('Glendale Heights', 'Village', '34208', 'DuPage'),
('Pekin', 'City', '34094', 'Tazewell'),
('Northbrook', 'Village', '33170', 'Cook'),
('Elk Grove Village', 'Village', '33127', 'Cook'),
('Danville', 'City', '33027', 'Vermilion'),
('St. Charles', 'City', '32974', 'Kane'),
('Woodridge', 'Village', '32971', 'DuPage'),
('North Chicago', 'City', '32574', 'Lake'),
('Galesburg', 'City', '32195', 'Knox')]
    if k == 1:
        return random.choice(cities)
    return random.sample(cities, k)

def make_set(source_fn, min, max):
    count = random.randint(min, max)
    return set(source_fn(count))

def lorem_ipsum_sentence():
    lorem = ['Cras volutpat, lacus quis semper pharetra.', 'Nisi enim dignissim est, et sollicitudin quam ipsum vel mi.', 'Sed commodo urna ac urna.', 'Nullam eu tortor.', 'Curabitur sodales scelerisque magna.', 'Donec ultricies tristique pede.', 'Nullam libero.', 'Nam sollicitudin felis vel metus.', 'Nullam posuere molestie metus.', 'Nullam molestie, nunc id suscipit rhoncus.',  'Felis mi vulputate lacus, a ultrices tortor dolor eget augue.', 'Aenean ultricies felis ut turpis.', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit.', 'Suspendisse placerat tellus ac nulla.', 'Proin adipiscing sem ac risus.']
    return random.choice(lorem)

def lorem_ipsum_fragment():
    lorem = ['Cras volutpat in diam.', 'Lacus quis semper pharetra.', 'Nisi enim dignissim est.', 'Sollicitudin quam ipsum vel mi.', 'Sed commodo urna ac urna.', 'Nullam eu tortor.', 'Curabitur sodales scelerisque magna.', 'Donec ultricies tristique pede.', 'Nullam libero frie.', 'Nam sollicitudin felis vel metus.', 'Nullam posuere molestie metus.', 'Nullam molesta vocum aria.', 'Nunc id suscipit rhoncus.',  'Felis mi vulputate lacus.', 'A ultrices tortor dolor eget augue.', 'Aenean ultricies felis ut turpis.', 'Lorem ipsum dolor sit amet.', 'Consectetuer adipiscing elit.', 'Suspendisse placerat tellus ac nulla.', 'Proin adipiscing sem ac risus.', 'Aliquam convallis neque vitae diam.', 'In diam cum sociis natoque.', 'Penatibus et magnis dis parturient montes', 'Nascetur ridiculus mus.', 'Duis fermentum arcu in tortor.', 'Sed nibh leo rhoncus eu.']
    return random.choice(lorem)


def random_quote(k = 1, quotes_only = True):
    quotes = {
"Always remember that you are absolutely unique. Just like everyone else.": 'Margaret Mead',
"Do not go where the path may lead, go instead where there is no path and leave a trail.": 'Ralph Waldo Emerson',
"Don't judge each day by the harvest you reap but by the seeds that you plant.": 'Robert Louis Stevenson',
"Dreaming, after all, is a form of planning.": 'Gloria Steinem',
"Go confidently in the direction of your dreams! Live the life you've imagined.": 'Henry David Thoreau',
"I attribute my success to this: I never gave or took any excuse.": 'Florence Nightingale',
"I didn't fail the test. I just found 100 ways to do it wrong.": 'Benjamin Franklin',
"I find that the harder I work, the more luck I seem to have.": 'Thomas Jefferson',
"I would rather die of passion than of boredom.": 'Vincent van Gogh',
"If life were predictable it would cease to be life and be without flavor.": 'Eleanor Roosevelt',
"If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.": 'James Cameron',
"If you're offered a seat on a rocket ship, don't ask what seat! Just get on.": 'Sheryl Sandberg',
"In the end, it's not the years in your life that count. It's the life in your years.": 'Abraham Lincoln',
"In this life we cannot do great things. We can only do small things with great love.": 'Mother Teresa',
"It is during our darkest moments that we must focus to see the light.": 'Aristotle',
"Life is a succession of lessons which must be lived to be understood.": 'Ralph Waldo Emerson',
"Life is either a daring adventure or nothing at all.": 'Helen Keller',
"Life is never fair, and perhaps it is a good thing for most of us that it is not.": 'Oscar Wilde',
"Life is what happens when you're busy making other plans.": 'John Lennon',
"Live in the sunshine, swim the sea, drink the wild air.": 'Ralph Waldo Emerson',
"Many of life's failures are people who did not realize how close they were to success when they gave up.": 'Thomas A. Edison',
"Never let the fear of striking out keep you from playing the game.": 'Babe Ruth',
"Only a life lived for others is a life worthwhile.": 'Albert Einstein',
"Spread love everywhere you go. Let no one ever come to you without leaving happier.": 'Mother Teresa',
"Success is not final; failure is not fatal: It is the courage to continue that counts.": 'Winston S. Churchill',
"Tell me and I forget. Teach me and I remember. Involve me and I learn.": 'Benjamin Franklin',
"The best and most beautiful things in the world cannot be seen or even touched: ' they must be felt with the heart.": 'Helen Keller',
"The future belongs to those who believe in the beauty of their dreams.": 'Eleanor Roosevelt',
"The greatest glory in living lies not in never falling, but in rising every time we fall.": 'Nelson Mandela', 
"The only impossible journey is the one you never begin.": 'Tony Robbins',
"The purpose of our lives is to be happy.": 'Dalai Lama',
"The secret of success is to do the common thing uncommonly well.": 'John D. Rockefeller Jr.',
"The way to get started is to quit talking and begin doing.": 'Walt Disney',
"Whatever the mind of man can conceive and believe, it can achieve.": 'Napoleon Hill',
"When you reach the end of your rope, tie a knot in it and hang on.": 'Franklin D. Roosevelt',
"Whoever is happy will make others happy too.": 'Anne Frank',
"You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.": 'Dr. Seuss',
"You only live once, but if you do it right, once is enough.": 'Mae West',
"You will face many defeats in life, but never let yourself be defeated.": 'Maya Angelou',
    }
    qlist = random.sample(quotes.keys(), k)
    if not quotes_only:
        return { key : quotes[key] for key in qlist }
    if k == 1:
        return qlist[0]
    return qlist