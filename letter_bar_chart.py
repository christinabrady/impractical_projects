import re
from collections import defaultdict
import pprint
pp = pprint.PrettyPrinter(indent=4)

print("Welcome to the poor man's bar chart")

user_input = input("Please give me a sentence.\n")
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def letter_count(sentence):
    ''' This function takes a string, counts the number of times
        each letter appears, and returns a stem and leaf plot
        of the letter appearances.
    '''
    mapped = defaultdict(list)
    for char in sentence:
        if char in ALPHABET:
            mappedsd[char].append(char)
    pp.ppint(mapped)

letter_count(user_input)
