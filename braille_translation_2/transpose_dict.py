# script for fixing my silly mistake
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

def dict_repr(dictionary):
	print('{')
	for key in dictionary:
		print('    \'' + key + '\':\'' + dictionary[key] + '\',')
	print('}')

def transpose_dict():
	new_braille_alphabet = {}
	for letter in braille_alphabet:
		new_braille_alphabet[letter] = braille_alphabet[letter][::3] + braille_alphabet[letter][1::3] + braille_alphabet[letter][2::3]
	dict_repr(new_braille_alphabet)

output = {
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
