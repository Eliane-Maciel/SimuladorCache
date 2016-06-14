# -*- coding: utf-8 -*-

def leituraArquivo():
    arquivo = open('./testsimples.cache', 'r')
    enderecos = arquivo.readlines()
    arquivo.close()

    return enderecos
