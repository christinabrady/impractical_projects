### look for anagrams for a given word
from collections import defaultdict
import load_dictionary

word_list = load_dictionary.load('/usr/share/dict/web2')
words = set(word_list)

words_x_len = defaultdict(list)
for word in words:
    words_x_len[len(word)].append(word)

user_input = input("What is your word?\n")

def find_anagrams(input):
    """
    take a word as direct input from user
    and return a list of anagrams
    """
    ## convert the word to a list so that the letters can be sorted
    input_sorted = list(input.lower())
    input_sorted.sort()
    ## grab all of the words from the dictionary that are the same length
    short_word_list = words_x_len[len(input)]
    short_word_list = set(short_word_list) ## to make it run faster
    ## sort the letters of the words from the dictionary and compare to the input sorted
    anagram_list = []
    for word in short_word_list:
        word_sorted = list(word)
        word_sorted.sort()
        if input_sorted == word_sorted:
            anagram_list.append(word)
    return(anagram_list)

anagrams = find_anagrams(user_input)

if len(anagrams) == 0:
    print("this word is unique")
else:
    print("Anagrams =", *anagrams, sep = "\n")
