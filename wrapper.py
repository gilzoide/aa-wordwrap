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


    def calculaMenorEspacosRemanescentesRecursivo (self):
        """Calcula o mínimo de espaços remanescentes, obedecendo a
relação de recorrência achada (inclusive feito pra testá-la).
Chama OPT com a última palavra e total de espaçoes"""
        return self.OPT (len (self.words) - 1, self.tam_maximo_linha)


    def OPT (self, palavra, pos, pulou = True):
        """OPT, o trem da recorrência recursivo; pulou diz se pulou linha"""
        # caso base
        if palavra < 0:
            return pos ** 2


        # tem que pular linha pra por essa mesma palavra
        tamanho_palavra = len (self.words[palavra])
        if tamanho_palavra > pos:
            return pos ** 2 + self.OPT (palavra, self.tam_maximo_linha)

        # se pos na mesma linha, e não for pular denovo, tira um do próximo
        # 'pos', já que tem que pular um espaço ;]
        if not pulou:
            dec = 1
        else:
            dec = 0

        # pôs essa, daí a príxima
        return min (
                # não pula linha
                self.OPT (palavra - 1, pos - tamanho_palavra - dec, False),
                # pula linha
                (pos - tamanho_palavra) ** 2 + self.OPT (palavra - 1, self.tam_maximo_linha))
