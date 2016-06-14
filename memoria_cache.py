# -*- coding: utf-8 -*-
from datetime import datetime
from random import randint

class Linha:
    """Class object linha"""
    rotulo = ''
    enderecoTotal = ''
    lru = ''

    def __init__(self, rotulo, enderecoTotal):
        self.rotulo = rotulo
        self.enderecoTotal = enderecoTotal


class Conjunto:
    linha = []
    conjunto = ''
    tamanho = 0
    prox = 0

    def __init__(self, qtdeLinhas):
        linhas = []
        tamanho = qtdeLinhas
        prox = 0

    def getConjunto(self):
        return self.conjunto

    def setConjunto(self, conjunto):
        self.conjunto = conjunto

    def procuraRotulo(rotuloEndereco):
        for linha in linhas:
            if linhas.rotulo == rotuloEndereco:
                data = datetime.now()
                linha.lru(data)
                return true
        return false

    def gravaRotulo(self, rotuloEndereco, politicaSubstituicao, politicaGravacao, mp, enderecoTotal):
        if self.prox == self.tamanho:
            if politicaSubstituicao == 0: #LRU
                poslinhaMenosRecUsada = buscaUltimaUsada()
                data = datetime.now()
                linha_object = Linha(rotuloEndereco, enderecoTotal)
                linha_object.lru = data
                del self.linha[poslinhaMenosRecUsada]
                self.linha.insert(poslinhaMenosRecUsada, linha_object)
                if politicaGravacao == 1:
                    mp.adicionaNaMP(linha_object.enderecototal)
            else: #Aleatorio
                linhaAleatoria = randint(0, self.tamanho)
                if politicaGravacao == 1:
                    mp.adicionaNaMP(linha[linhaAleatoria].enderecoTotal)
                linhas[linhaAleatoria] = Linha(rotuloEndereco, enderecoTotal)
                data = datetime.now()
                linhas[linhaAleatoria].lru(data)
        else:
            data = datetime.now()
            linha_object = Linha(rotuloEndereco, enderecoTotal)
            linha_object.lru(data)
            self.linha.append(linha_object)
            self.prox = self.prox + 1

    def buscaUltimaUsada(self):
        aux = linha[0].lru
        menosUsado = 0
        for i, x in enumerate(testlist):
            if x.lru < aux:
                aux = x.lru
                menosUsado = i
        return menosUsado

class MemoriaCache:
    conjuntos = []
    tamanho = 0
    proximo = 0

    def __init__(self, qtdeConjuntos, qtdeLinhas):
        self._tamanho = qtdeConjuntos
        for i in range(0, qtdeConjuntos):
            self.conjuntos.append(Conjunto(qtdeLinhas))
        proximo = 0


    def setConjuntos(self, conjuntos):
        self.conjuntos = conjuntos

    def getConjuntos(self):
        return self.conjuntos

    def procuraConjunto(self, enderecoConjunto):
        for i in range(0, self.proximo):
            if conjuntos[i].getConjunto() == enderecoConjunto:
                return conjuntos[i]
        return False

    def gravaConjunto(self, enderecoConjunto):
        if self.proximo != self.tamanho:
            self.conjuntos[self.proximo].setConjunto(enderecoConjunto)
            proximo += 1

            return self.conjuntos[self.proximo-1]
        return None

class MemoriaPrincipal:
    enderecos = []
    total = 0

    def __init__(self):
        self.enderecos = []
        self.total = 0

    def adicionaNaMP(self, enderecoTotal):
        self.enderecos.append(enderecoTotal)
        self.total += 1

    def buscaNaMP(self, enderecoTotal):
        for i in self.enderecos:
            if i == enderecoTotal:
                return True
        return False
