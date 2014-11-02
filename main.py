#!/bin/env pypy3
# coding: utf-8

# 1ª linha permite rodar o script direto pelo shell;
# preferência pelo pypy que é mais rápido
# 2ª pro trem saber que aqui é raça utf-8!

# Gil Barbosa Reis - 8532248
# Leonardo Sampaio Ferraz Ribeiro - 8532300
# SCC 0218 - Algoritmos Avançados e Aplicações

import sys
from wrapper import Wrapper

teste = Wrapper ()
teste.getInput (sys.stdin)
teste.imprimeSaida ()

print (teste.calculaMenorEspacosRemanescentesRecursivo ())
