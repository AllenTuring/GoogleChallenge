# lowercase braille alphabet
braille_alphabet = {
    'a':'10000000',
    'b':'11000010',
    'c':'10010000',
    'd':'10011000',
    'e':'10001000',
    'f':'11010010',
    'g':'11011010',
    'h':'11001010',
    'i':'01010010',
    'j':'01011010',
    'k':'10100001',
    'l':'11100011',
    'm':'10110001',
    'n':'10111001',
    'o':'10101001',
    'p':'11110011',
    'q':'11111011',
    'r':'11101011',
    's':'01110011',
    't':'01111011',
    'u':'10100101',
    'v':'11100111',
    'w':'01011110',
    'x':'10110101',
    'y':'10111101',
    'z':'10101101',
    ' ':'00000000',
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
