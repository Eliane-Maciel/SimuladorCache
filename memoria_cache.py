# -*- coding: utf-8 -*-
from datetime import datetime

class Linha:
    """Class object linha"""
    rotulo = ''
    enderecoTotal = ''
    lru = ''

    def __init__(self, rotulo):
        self.rotulo = None


class Conjunto:
    linha = []
    conjunto = ''
    tamanho = 0
    prox = 0

    def procuraRotulo(rotuloEndereco):
        for linha in linhas:
            if linhas.rotulo == rotuloEndereco:
                data = datetime.now()
                linha.lru(data);
                return true;
        return false

    def gravaRotulo(rotuloEndereco, politicaSubstituicao, politicaGravacao, MemoriaPrincipal mp, String enderecoTotal):
        if prox == tamanho:
            if politicaSubstituicao == 0: #LRU
                linhaMenosRecUsada = buscaUltimaUsada()
                if politicaGravacao == 1:
                    mp.adicionaNaMP(linhas[linhaMenosRecUsada].enderecototal);
                }
                linhas[linhaMenosRecUsada].rotulo = rotuloEndereco
                linhas[linhaMenosRecUsada].enderecoTotal = enderecoTotal

                data = datetime.now()
                linhas[linhaMenosRecUsada].lru(data)
            else: #Aleatorio
                # linhaAleatoria = (int) (Math.random() * tamanho+0);
                if politicaGravacao == 1:
                    # mp.adicionaNaMP(linhas[linhaAleatoria].getEnderecoTotal());
                    pass
                # linhas[linhaAleatoria].setRotulo(rotuloEndereco, enderecoTotal);
                data = datetime.now()
                # linhas[linhaAleatoria].lru(data);
        else:
            data = datetime.now()
            linhas[prox] = Linha();
            linhas[prox].rotulo = rotuloEndereco
            linhas[prox].enderecoTotal = enderecoTotal
            linhas[prox].lru(data);
            prox = prox + 1

    def conjunto_qt(qtdeLinhas):
        linhas = Linha[qtdeLinhas];
        tamanho = qtdeLinhas;
        prox = 0

    def buscaUltimaUsada():
        aux = linhas[0].lru
        menosUsado = 0
        for i in linhas:
            # if(linhas[i].getLru().compareTo(aux) < 0){
            #     aux = linhas[i].getLru();
            #     menosUsado = i;
            # }
        return menosUsado;

class MemoriaCache:
    conjuntos = []
    tamanho = 0
    proximo = 0

    def memoriaCache(qtdeConjuntos, qtdeLinhas):
        tamanho = qtdeConjuntos;
        conjuntos = Conjunto[];
        for i in conjuntos:
            # conjuntos[i] = new Conjunto(qtdeLinhas);
        proximo = 0

    def procuraConjunto(enderecoConjunto):
        # for(int i=0;i<proximo;i++){
        #     if(conjuntos[i].getConjunto().equals(enderecoConjunto)){
        #         return conjuntos[i];
        #     }
        # }
        return None

    def gravaConjunto(enderecoConjunto):
        # if(proximo != tamanho){
        #     conjuntos[proximo].setConjunto(enderecoConjunto);
        #     proximo++;
        #     return conjuntos[proximo-1];
        # }
        return None


class MemoriaPrincipal:
    enderecos = []
    total = 0

    def buscaNaMP(enderecoTotal):
        # for(int i=0;i<total;i++){
        #     if(enderecos.get(i).equals(enderecoTotal)){
        #         return true;
        #     }
        # }
        return false
