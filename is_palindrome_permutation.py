# Write an efficient function that checks whether any permutation of an input string is a palindrome.
# Assumptions -
# 1. Only lower case letters.
# 2. Input is always valid, i.e. no empty strings.

# Solution -
# 1. If only one letter, return True.
# 2. If odd number of letters:
# 		return True if every letter except one has a matching letter in the string.
# 3. If even number of letters:
#     return True is every letter has a matching letter in the string.

# Examples -
# 1. a = True
# 2. aa = True
# 3. ab = False
# 4. aabba = True
# 5. bbbbbb = True

# Runtime -
# n is length of string, so O(n) to add all chars to a dictionary
# Worst case O(n) to go through dictionary and find unmatched characters
# O(1) to check length of unmatched characters
# O(n)


def is_palindrome_permutation(string):

    if string is None or not isinstance(string, str):
        return False

    if len(string) == 1:
        return True

    word_dict = {}
    for char in string:
        if char in word_dict.keys():
            word_dict[char] = word_dict[char] + 1
        else:
            word_dict[char] = 1

    unmatched_characters = find_unmatched_characters(word_dict)

    if len(unmatched_characters) <= 1:
        return True
    else:
        return False


def find_unmatched_characters(_word_dict):

    return [key for key in _word_dict if _word_dict[key] % 2 == 1]


if __name__ == '__main__':

    strings = ['civic',
               'civil',
               'a',
               'dog',
               'abacus',
               'ababababa',
               'aaa',
               'bbbb']
    for string in strings:
        print(string + ' = ' + is_palindrome_permutation(string).__str__())
