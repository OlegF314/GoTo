def f(string):
    edited_string = ''
    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    NEXT_C = ['b', 'f', 'j', 'p', 'v', 'z']
    for letter in string:
        if letter in VOWELS:
            edited_string += NEXT_C[VOWELS.index(letter)]
        elif letter in ALPHABET:
            edited_string += str(ALPHABET.index(letter))
        else:
            edited_string += letter
    return  edited_string