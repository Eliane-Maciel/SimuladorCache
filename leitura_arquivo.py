# -*- coding: utf-8 -*-

__author__ = "Eliane Isadora Faveron Maciel"


def leituraArquivo():
    arquivo = open('./oficial.cache', 'r')
    enderecos = arquivo.readlines()
    arquivo.close()

    return enderecos
