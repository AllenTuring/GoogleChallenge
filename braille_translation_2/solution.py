# lowercase braille alphabet
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
        ' ':'000000',
    }
braille_uppercase = '000001'

def answer(plaintext):
    # string to hold our braille representation
    braille_representation = ''
    for char in plaintext:
        if char.isupper():
            braille_representation += braille_uppercase
        braille_representation += braille_alphabet[char.lower()]
    # output
    return braille_representation

def test():
    # unit tests
    assert answer("code") == "100100101010100110100010"
    assert answer("Braille") == "000001110000111010100000010100111000111000100010"
    assert answer("The quick brown fox jumped over the lazy dog") == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"
