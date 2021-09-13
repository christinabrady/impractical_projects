import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

print("Welcome to the poor man's bar chart")

user_input = input("Please give me a sentence.\n")

def letter_count(sentence):
    ''' This function takes a string, counts the number of times
        each letter appears, and returns a stem and leaf plot
        of the letter appearances.
    '''

    no_punct = re.sub(r'[^\w\s]+', '', sentence.lower())
    no_new_line = re.sub('\\n', '', no_punct)
    no_space = re.sub(r'\s+', '', no_new_line)
    chars = list(no_space)
    chars.sort()
    keylist = set(chars)
    d = {}
    for key in keylist:
        d[key] = [char for char in chars if char == key]
    pp.pprint(d)

letter_count(user_input)
