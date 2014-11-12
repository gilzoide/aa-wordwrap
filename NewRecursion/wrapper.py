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

	def __init__ (self, words, line_length):
		"""Constructor that gets a list of words' sizes and the line length"""
		
		self.word_sizes = []
		self.line_length = line_length
		self.words = words

		# count the words' lengths
		words_size = []
		for word in words:
			self.word_sizes.append(len(word))	

	def build_remaining_spaces_matrix(self):
		"""Builds a matrix with n^2 size where P[i, j] is the squared number of remaining
	spaces if a line is made with words i to j"""

		# create the matrix
		remaining_spaces = []; self.line_costs = []
		for i in range(len(self.word_sizes)):
			remaining_spaces.append([0]*len(self.word_sizes))
			self.line_costs.append([0]*len(self.word_sizes))

		for i in range(len(self.word_sizes)):

			# line with only one word
			remaining_spaces[i][i] = self.line_length - self.word_sizes[i]

			# calculate the remainig with lines from i to j
			# taking the whitespace into account (-1)
			for j in range(i + 1, len(self.word_sizes)):
				remaining_spaces[i][j] = remaining_spaces[i][j-1] - self.word_sizes[j] - 1

		# create the cost matrix, the one really used
		for i, row in enumerate(remaining_spaces):
			for j, spaces in enumerate(row):
				if spaces < 0:
					self.line_costs[i][j] = 999
				else:
					self.line_costs[i][j] = spaces**2


	
	def dynamic_programming(self):
		"""Apply Dynamic Programming techniques to solve the problem. Based on the 
	recurrence function explained in the .PDF file."""

		self.build_remaining_spaces_matrix()

		# auxiliaries
		minimum = 0
		self.OPT = [0]

		# dynamic programming loop
		for j in range(1, len(self.line_costs)+1):
			cost_of_line_break = []
			for i in range(1, j+1):
				cost_of_line_break.append(self.OPT[i - 1] + self.line_costs[i-1][j-1])
			self.OPT.append(min (cost_of_line_break))

		print("\nOPT: ", self.OPT)


	def print_word_wrapped(self):
		"""Print the words in the new lines, based on the premise that after a line break, 
		the OPT value increases"""

		for i in range(len(self.words)-1):

			# if the next is bigger, we have a line break
			if self.OPT[i] < self.OPT[i+1]:
				end = '\n'
			else:
				end = ' '

			print (self.words[i], end = end)

		# print remainig + new line
		print (self.words[-1])














