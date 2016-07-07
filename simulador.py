# -*- coding: utf-8 -*-

from memoria_cache import *
from leitura_arquivo import leituraArquivo
import sys
import os


def gravaDados():
    os.system('cls' if os.name == 'nt' else 'clear')
    politicaEscrita = int(raw_input(
        '\tPolitica de Escrita : 0 - write-through;\t1 - write-back; ')
    )
    tamanhoDaLinha = int(raw_input('\tTamanho da Linha : '))
    numeroDeLinhas = int(raw_input('\tNúmero de linhas: '))
    linhasPorConjunto = int(raw_input('\tAssossiatividade por conjunto: '))
    tempoAcesso = int(raw_input(
        '\tTempo de acesso quando encontra (hit-time): ')
    )
    politicaSubstituicao = int(raw_input(
        '\tPolitica de Substituição: 0 - LFU;\t1 - LRU;\t2 - Aleatório;')
    )

    tempoMP = int(raw_input('\tTempo de leitura/escrita:'))

    memoriaPrincipal = MemoriaPrincipal()
    qtdeConjuntos = numeroDeLinhas/linhasPorConjunto
    tamanhoTotalDaCache = numeroDeLinhas * tamanhoDaLinha
    # Calcula o tamanho do endereço do conjunto;
    resto = 0
    aux = qtdeConjuntos
    tamanhoEnderecoConjunto = 0
    while resto != 1:
        aux = aux/2
        resto = aux
        tamanhoEnderecoConjunto += 1

    # Calcula o tamanho do endereço da palavra
    resto = 0
    aux = tamanhoDaLinha
    enderecoPalavra = 0
    while resto != 1:
        aux = aux/2
        resto = aux
        enderecoPalavra += 1

    # Calcula o rótulo
    rotulo = 32 - (enderecoPalavra + tamanhoEnderecoConjunto)
    memoriaCache = MemoriaCache(qtdeConjuntos, linhasPorConjunto)
    enderecos = leituraArquivo()
    leituras = 0
    escritas = 0
    leiturasNaCache = 0
    leiturasNaMP = 0
    escritasNaCache = 0
    escritasNaMP = 0
    encontrouNaCacheLeitura = 0
    encontrouNaCacheEscrita = 0
    encontrouNaMPLeitura = 0
    encontrouNaMPEscrita = 0
    for end in enderecos:
        atributos = end.split(' ')
        endereco = atributos[0]
        operacao = atributos[1]
        # Transforma em binário
        my_hexdata = endereco
        scale = 16
        # equals to hexadecimal
        num_of_bits = 32
        endBinario = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
        rotuloEndereco = endBinario[0:rotulo]
        enderecoConjunto = endBinario[
            rotulo+1:rotulo+1+tamanhoEnderecoConjunto
        ]
        operacao = operacao.replace('\n', '')
        if operacao == "R":
            conjunto = memoriaCache.procuraConjunto(enderecoConjunto)
            leituras += 1
            # Contador de leituras
            leiturasNaCache += 1
            if conjunto:
                # Procura rotulo pelo conjunto encontrado
                retornoRotulo = conjunto.procuraRotulo(rotuloEndereco)
                if retornoRotulo:
                    # Se encontrou o rótulo ocorre hit
                    encontrouNaCacheLeitura += 1
                else:
                    # Caso não encontrou o rótulo da erro
                    conjunto.gravaRotulo(
                        rotuloEndereco, politicaSubstituicao, politicaEscrita,
                        memoriaPrincipal, endBinario
                    )
                    leiturasNaMP += 1
                    encontrouNaMPLeitura += 1
            else:
                conjunto = memoriaCache.gravaConjunto(enderecoConjunto)
                if conjunto:
                    conjunto.gravaRotulo(
                        rotuloEndereco, politicaSubstituicao, politicaEscrita,
                        memoriaPrincipal, endBinario
                    )
                leiturasNaMP += 1
                encontrouNaMPLeitura += 1
        else:
            escritas += 1
            conjunto = memoriaCache.procuraConjunto(enderecoConjunto)
            escritasNaCache += 1
            if not conjunto:
                conjunto = memoriaCache.gravaConjunto(enderecoConjunto)
                conjunto.gravaRotulo(
                    rotuloEndereco, politicaSubstituicao, politicaEscrita,
                    memoriaPrincipal, endBinario
                )
            else:
                retornoRotulo = conjunto.procuraRotulo(rotuloEndereco)
                if not retornoRotulo:
                    conjunto.gravaRotulo(
                        rotuloEndereco, politicaSubstituicao, politicaEscrita,
                        memoriaPrincipal, endBinario
                    )
                else:
                    encontrouNaCacheEscrita += 1
            if politicaEscrita == 0:
                escritasNaMP += 1
                encontrouNaMPEscrita += 1

    totalDeRegistros = leituras + escritas
    # Seta total de escritas;
    totalDeEscritas = escritas
    totalDeLeituras = leituras
    taxaDeAcertoCacheLeitura = 0
    # Acerto Leitura Cache
    if leiturasNaCache:
        taxaDeAcertoCacheLeitura = (
            (encontrouNaCacheLeitura*100.0)/leiturasNaCache
        )
    # Acerto Leitura MP
    if leiturasNaMP:
        taxaDeAcertoMPLeitura = (encontrouNaMPLeitura*100.0)/leiturasNaMP
    if escritasNaCache:
        taxaDeAcertoCacheEscrita = (
            (encontrouNaCacheEscrita*100.0)/escritasNaCache
        )
    totalLeituraEscrita = (
        float(encontrouNaCacheLeitura)+float(encontrouNaCacheEscrita)
    )
    taxaAcerto = totalLeituraEscrita / (leiturasNaCache + escritasNaCache)
    tempoMedio = 0.0
    if taxaDeAcertoCacheLeitura:
        t1 = tempoAcesso
        # tempoMedio = t1+ (1-h)*t2
        h_taxa = taxaAcerto
        tempoMedio = t1 + ((1 - h_taxa) * tempoMP)
    taxaAcerto = taxaAcerto * 100.0
    tempoMedio = format(tempoMedio, '.2f')
    taxaDeAcertoCacheLeitura = format(taxaDeAcertoCacheLeitura, '.4f')
    taxaDeAcertoCacheEscrita = format(taxaDeAcertoCacheEscrita, '.4f')
    taxaAcerto = format(taxaAcerto, '.4f')

    os.system('cls' if os.name == 'nt' else 'clear')
    texto = ""
    texto += "\nDADOS DE ENTRADA:\n"
    if politicaEscrita == 0:
        texto += "Politica de Escrita: " + str(politicaEscrita)
        texto += " - write-through\n"
    else:
        texto += "Politica de Escrita: " + str(politicaEscrita)
        texto += " - write-back\n"
    texto += "Tamanho da linha: " + str(tamanhoDaLinha) + ", \n"
    texto += "Numero de linhas: " + str(numeroDeLinhas) + ", \n"
    texto += "Associatividade por conjunto: " + str(linhasPorConjunto) + "\n"
    texto += "Tempo de Acesso na Cache: " + str(tempoAcesso) + ", \n"

    if politicaSubstituicao == 0:
        texto += "Politica de Substituição: " + str(politicaSubstituicao)
        texto += " - LFU\n"
    elif politicaSubstituicao == 1:
        texto += "Politica de Substituição: " + str(politicaSubstituicao)
        texto += " - LRU\n"
    else:
        texto += "Politica de Substituição: " + str(politicaSubstituicao)
        texto += " - Aleatorio\n"

    texto += "Tempo de Acesso na memória principal: " + str(tempoMP) + "ns\n"

    texto += "\nRESULTADOS:\n"
    texto += "Tamanho da Cache: " + str(tamanhoTotalDaCache) + "\n"
    texto += "Total de endereços no arquivo de entrada:\n"
    texto += "Total de registros: " + str(totalDeRegistros) + "\n"
    texto += "Total de leituras: " + str(totalDeLeituras) + "\n"
    texto += "Total de escritas: " + str(totalDeEscritas) + "\n"

    texto += "Dados da Cache:\n"
    texto += "Total de leituras: " + str(leiturasNaCache) + "\n"
    texto += "Total de acertos: " + str(encontrouNaCacheLeitura) + "\n"
    texto += "Taxa de acerto Leitura: " + str(taxaDeAcertoCacheLeitura) + "%\n"

    texto += "Total de escritas: " + str(escritasNaCache) + "\n"
    texto += "Total de acertos: " + str(encontrouNaCacheEscrita) + "\n"
    texto += "Taxa de acerto Escrita: "+str(taxaDeAcertoCacheEscrita) + "%\n"

    texto += "Taxa de acertos: " + str(taxaAcerto) + "%\n"
    texto += "Tempo médio de acesso da cache: " + str(tempoMedio) + "ns\n"

    texto += "Dados da Memória Principal:\n"
    texto += "Total de escritas: " + str(encontrouNaMPEscrita) + "\n"
    texto += "Total de leituras: " + str(encontrouNaMPLeitura) + "\n"
    texto += "Acessos: " + str(leiturasNaMP+escritasNaMP) + "\n"

    print texto

    EscreveResultados(texto)

    return


def EscreveResultados(texto):
    arquivo = open('./results.txt', 'w')
    arquivo.writelines(texto)
    arquivo.close()
    return


def main():
    gravaDados()
    return


if __name__ == '__main__':
    main()
