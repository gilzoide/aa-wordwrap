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
words = user_input.split()
line_length = int(words[0])
words.pop(0)

# create a new word wrapper object
wrapper = Wrapper(words, line_length)
wrapper.dynamic_programming()
wrapper.print_word_wrapped()

