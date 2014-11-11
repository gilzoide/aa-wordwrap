# coding: utf-8
#
# SCC0218 [Algoritmos Avançados e Aplicações]
# Projeto 2 - Wordwrapping with DP
#
# Gil Barbosa Reis 	 				NUSPº 8532248
# Leonardo Sampaio Ferraz Ribeiro 	NUSPº 8532300

class Wrapper:

	"""Word Wrapper, optimized based on the minimization of
	the sum of squared remaining spaces"""

	"""Constructor that gets a list of words' sizes and the line length"""
	def __init__ (self, words, line_length):
		self.words = words
		self.line_length = line_length	

	"""Builds a matrix with n^2 size where P[i, j] is the squared number of remaining
	spaces if a line is made with words i to j"""
	def build_remaining_spaces_matrix():

		# create the matrix
		remaining_spaces = []
		for i in range(len(words)):
			remaining_spaces.append([0]*len(words))

		for i in range(len(words)):

			# line with only one word
			remaining_spaces[i][i] = line_length - words[i]

			# calculate the remainig with lines from i to j
			# taking the whitespace into account (-1)
			for j in range(i + 1, len(words)):
				remaining_spaces[i][j] = remaining_spaces[i][j-1] - words[j] - 1

	

