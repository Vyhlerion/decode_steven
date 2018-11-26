#! /usr/bin/python3
""" Decodes the Steven code """

import re
import string

def combinations(length: int = 1, charset='01'):
    """ Generate all possible combinations of length 'length'
	for the charset 'charset' """
    if length < 2:
        return charset
    return [head+tail\
		for head in charset\
		for tail in combinations(length - 1, charset)]

raw_message = "00110-01001-01110-00100 01101-00101"
message = re.findall(r"[\w']+", raw_message)

code = {key:value for key, value in\
	zip(combinations(5, '01')[1:], string.ascii_lowercase)}

decoded = raw_message
for letter in message:
    decoded = decoded.replace(letter, code[letter])

print(raw_message, "->", decoded, "->", decoded.replace("-", ""))
