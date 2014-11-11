# coding: utf-8
#
# SCC0218 [Algoritmos Avançados e Aplicações]
# Projeto 2 - Wordwrapping with DP
#
# Gil Barbosa Reis                  NUSPº 8532248
# Leonardo Sampaio Ferraz Ribeiro   NUSPº 8532300

from wrapper import Wrapper
import sys

# auxiliar
user_input = ""

# read input until EOF
for line in sys.stdin:
	user_input += line 

# split output and separate length from words
splitted_input = user_input.split()
line_length = int(splitted_input[0])
words = splitted_input[1:len(splitted_input)]

# count the words' lengths
words_size = []
for word in words:
	words_size.append(len(word))

# create a new word wrapper object
wrapper = Wrapper(words_size, line_length)

print(line_length, words, words_size)
