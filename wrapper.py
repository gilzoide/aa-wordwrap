# coding: utf-8

# Gil Barbosa Reis - 8532248
# Leonardo Sampaio Ferraz Ribeiro - 8532300
# SCC 0218 - Algoritmos Avançados e Aplicações

class Wrapper:
    """TAD do Word Wrapper, que processa a entrada das palavras otimizado
em relação aos quadrados dos espaços remanescentes"""
    def __init__ (self):
        self.words = []
        # o L do PDF
        self.tam_maximo_linha = 0

    def getInput (self, stream):
        """Lê a entrada linha a linha, e monta a lista de palavras"""
        # partition separa uma string pelo separador, e retorna 
        # a string antes, o separador em si e a string depois
        max_linha, sep, s = stream.readline ().partition (' ')
        self.tam_maximo_linha = int (max_linha)

        while s:
            # adiciona as palavras de 's' separadas por espaços em branco
            self.words.extend (s.split ())
            # lê mais uma linha
            s = stream.readline ()

    def imprimeSaida (self):
        """Dá a saída do rolê"""
        print (self.words)
