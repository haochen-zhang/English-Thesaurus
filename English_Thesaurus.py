# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:22:14 2021
@author: Haochen Zhang
"""
import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        guess = get_close_matches(word.lower(), data.keys())
        if guess:
            respond = input('Did you mean %s instead? Please enter Y for yes and N for no: ' % guess[0])
            if respond.upper() == 'Y':
                return data[guess[0]]
            elif respond.upper() == 'N':
                return "The word doesn't exist. Please double check it."
            else:
                return "We don't understand your input"
        else:
            return "The word doesn't exist. Please double check it."

word = input('Enter word: ')

outputs = translate(word)
if type(outputs) == list:  
    for output in outputs:
        print(output)
else:
    print(outputs)

