import sys

def print_with_separator(message):
    print('-' * len(message))
    print(message)

def picker(message, options):
    print_with_separator(message)
    for idx, element in enumerate(options):
        print(f'{idx+1}. {element}')
    i = input('enter number: ')
    try:
        number = int(i)
        if 0 < int(i) <= len(options):
            return number
        else:
            raise ValueError('incorrect value')
    except:
        print('could not get correct input')
        sys.exit(1)
    
def get_file(message):
    try:
        print_with_separator(message)
        file_name = input()
        file = open(file_name)
        result = file.read()
        file.close()
        return (file_name, result)
    except:
        print('could not read file')
        sys.exit(1)

from nltk.tokenize import RegexpTokenizer

def tokenize(text):
    tokenizer = RegexpTokenizer("[\w']+")
    return tokenizer.tokenize(text)