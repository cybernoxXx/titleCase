import random


def getTitleCase(phrase):
    DICT_TO_UPPER = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J',
                     'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T',
                     'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z', }
    DICT_TO_LOWER = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
                     'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
                     'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z', }
    firstCharacter = True
    phraseList = list(phrase)

    for character in phraseList:
        # Case first character of the word
        if firstCharacter and character in DICT_TO_UPPER:
            # Taking the index of the actual character and converting the list's element into uppercase
            index = phraseList.index(character)
            phraseList[index] = DICT_TO_UPPER[character]
            firstCharacter = False
        # Case character uppercase in the word
        elif firstCharacter == False and character in DICT_TO_LOWER:
            # Taking the index of the actual character and converting the list's element into lowercase
            index = phraseList.index(character)
            phraseList[index] = DICT_TO_LOWER[character]
        # Case word delimiter
        elif character not in DICT_TO_LOWER and character not in DICT_TO_UPPER:
            # The next character will be the first one of the new word
            firstCharacter = True
        else:
            firstCharacter = False

    return ''.join(phraseList)


assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for i in range(1000):
    random.shuffle(chars)
    assert getTitleCase(''.join(chars)) == ''.join(chars).title()
