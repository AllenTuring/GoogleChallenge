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
        'test!': '135246',
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
    'a':'100000',
    'b':'100010',
    'c':'101000',
    'd':'111000',
    'e':'110000',
    'f':'101010',
    'g':'111010',
    'h':'110010',
    'i':'001010',
    'j':'011010',
    'k':'100100',
    'l':'100110',
    'm':'101100',
    'n':'111100',
    'o':'110100',
    'p':'101110',
    'q':'111110',
    'r':'110110',
    's':'001110',
    't':'011110',
    'u':'100101',
    'v':'100111',
    'w':'011011',
    'x':'101101',
    'y':'111101',
    'z':'110101',
    ' ':'000000',
    'test!':'123456',
}


