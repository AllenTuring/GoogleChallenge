# Generates the braille alphabet dictionary
def generate_braille_alphabet():
    # braille alphabet dictionary
    braille_alphabet = {
        'a':'100000',
        'b':'101000',
        'c':'110000',
        'd':'110100',
        'e':'100100',
        'f':'111000',
        'g':'111100',
        'h':'101100',
        'i':'011000',
        'j':'011100',
        'k':'100010',
        'l':'101010',
        'm':'110010',
        'n':'110110',
        'o':'100110',
        'p':'111010',
        'q':'111110',
        'r':'101110',
        's':'011010',
        't':'011110',
        'u':'100011',
        'v':'101011',
        'w':'011101',
        'x':'110011',
        'y':'110111',
        'z':'100111',
    }
    # generate capitals
    for letter, braille in braille_alphabet:
        braille_alphabet[letter.upper()] = '000001' + braille
    # add space
    braille_alphabet[' '] = '000000'

    # output
    return braille_alphabet

braille_alphabet = generate_braille_alphabet()

def answer(plaintext):
    # TODO stub
    print(braille_alphabet)
