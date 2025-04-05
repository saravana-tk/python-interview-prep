'''
Bob, Alice's friend, is also interested in string manipulations. Inspired by Alice's technique, he has devised his own string encoding scheme. He takes a sentence, which is a string of n alphanumeric characters (ranging from a-z, A-Z, 0-9), including spaces and punctuation marks, with n ranging from 1 to 500, inclusive. His encoding technique consists of the following steps:

He replaces each alphanumeric character with the previous character in their respective sequence, i.e., for alphabets, he moves in the alphabetical order, and for numbers, he moves in the ordinal sequence.

For instance, given a string word, for each character, if it's not a or A or 0, he replaces it with the character that precedes it in the sequence.
For the character a or A, he replaces it with z or Z, respectively.
For the number 0, he replaces it with 9.
Another important aspect of Bob's algorithm involves frequency analysis. After shifting the characters, he counts the frequency of each alphanumeric character in the new string. Then, he creates an association between each alphanumeric character and its frequency and ASCII value. Each character maps to a number, which is the difference between the ASCII value of the character and its frequency. Once this is done, he computes the absolute value of each of these differences.

The task is to help Bob generate a list of these absolute differences, sorted in ascending order.
'''

def solution(sentence):
    final_list = []
    intermediate_dictionary = {}
    for c in sentence:
        if c.isalpha():
            if c == 'a':
                updateDictionary(
                    intermediate_dictionary,
                    'z'
                )
            elif c == 'A':
                updateDictionary(
                    intermediate_dictionary,
                    'Z'
                )
            else:
                updateDictionary(
                    intermediate_dictionary,
                    chr(ord(c) - 1)
                )
        elif c.isdigit():
            if c == '0':
                updateDictionary(
                    intermediate_dictionary,
                    '9'
                )
            else:
                updateDictionary(
                    intermediate_dictionary,
                    str(int(c) - 1)
                )
    
    final_list = [ord(key) - value for key, value in intermediate_dictionary.items()]
    final_list.sort()
    return final_list


def updateDictionary(dictionary, char):
    dictionary[char] = dictionary.get(char, 0) + 1
    
    
print(solution("Hello, 123!"))