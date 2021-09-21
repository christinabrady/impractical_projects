"""Find all word-pair palingrams in a dictionary file."""

import load_dictionary
word_list = load_dictionary.load('/usr/share/dict/web2')

# find word-pair palingrams udef find_palingrams():
"""Find dictionary palingrams."""

def is_palindrome(string):
    """ first check if the string is a palingram """
    if len(string) <= 1:
        return True
    else:
        first = string[0]
        last = string[-1]
        if first == last:
            return is_palindrome(string[1:-1])
        else:
            return False

# is_palingram("rator")

def find_palidromes():
    pali_list = []
    words = set(word_list)
    for word in words:
        if is_palindrome(word):
            pali_list.append(word)
    return pali_list

palingrams = find_palidromes()
# sort palingrams on first word

palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
# for first, second in palingrams_sorted:
#     print("{} {}".format(first, second))

### testing purposes
# for word in word_list:
#     end = len(word)
#     rev_word = word[::-1]
#     if end > 1:
#         for i in range(end):
#             print(word[i:], sep = "\n")
#             print(rev_word[end-i:], sep = "\n")
