# -*- coding: utf-8 -*-

def leituraArquivo():
    arquivo = open('./teste.cache', 'r')
    enderecos = arquivo.readlines()
    arquivo.close()

    return enderecos
