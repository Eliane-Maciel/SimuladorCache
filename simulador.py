# -*- coding: utf-8 -*-
from memoria_cache import Linha, Conjunto, MemoriaCache, MemoriaPrincipal
from leitura_arquivo import leituraArquivo
# from interface import Application


def gravaDados():
    politicaEscrita = int(raw_input('Politica de Escrita : 0 - write-through  1 - write-back; '))
    tamanhoDaLinha = int(raw_input('Tamanho da Linha : '))
    numeroDeLinhas = int(raw_input('Número de linhas: '))
    linhasPorConjunto = int(raw_input('Assossiatividade por conjunto: '))
    tempoAcesso = int(raw_input('Tempo de acesso quando encontra (hit-time): '))
    politicaSubstituicao = int(raw_input('Politica de Substituição: 1 - LFU; 2 - LRU'))

    tempoMP = int(raw_input('Tempo de leitura/escrita:'))
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

    #Calcula o tamanho do endereço da palavra
    resto = 0
    aux = tamanhoDaLinha
    enderecoPalavra = 0
    while resto != 1:
        aux = aux/2
        resto = aux
        enderecoPalavra += 1

    #Calcula o rótulo
    rotulo = 32 - (enderecoPalavra + tamanhoEnderecoConjunto)
    memoriaCache = MemoriaCache(qtdeConjuntos, linhasPorConjunto)
    enderecos = leituraArquivo()
    leituras = 0
    escritas = 0
    leiturasNaCache = 0
    leiturasNaMP = 0
    escritasNaCache = 0
    escritasNaMP = 0
    naoEncontrouNaCacheLeitura = 0
    encontrouNaCacheLeitura = 0
    naoEncontrouNaCacheEscrita = 0
    encontrouNaCacheEscrita = 0
    naoEncontrouNaMPLeitura = 0
    encontrouNaMPLeitura = 0
    naoEncontrouNaMPEscrita = 0
    encontrouNaMPEscrita = 0

    for end in enderecos:
        atributos = end.split(' ')
        endereco = atributos[0];
        operacao = atributos[1];

        # Transforma em binário
        intEnd = int(endereco, 16);
        endBinario = bin(intEnd)
        endBinario = endBinario.replace("0b", "00")
        bin_32 = '00000000000000000000000000000000'
        #preenche com zeros na frente para ficar com 32 digitos
        endBinario = bin_32 + endBinario

        #Busca os endereços
        rotuloEndereco = endBinario[0:rotulo]
        enderecoConjunto = endBinario[rotulo+1:rotulo+1+tamanhoEnderecoConjunto]

        if operacao == "R":
            leituras +=1

            conjunto = memoriaCache.procuraConjunto(enderecoConjunto)

            #Contador de leituras
            leiturasNaCache += 1

            if conjunto:
                #Procura rotulo pelo conjunto encontrado
                retornoRotulo = conjunto.procuraRotulo(rotuloEndereco)
                if retornoRotulo:
                    #Se encontrou o rótulo ocorre hit
                    encontrouNaCacheLeitura += 1
                else:
                    #caso não encontrou o rótulo da erro
                    naoEncontrouNaCacheLeitura += 1
                    conjunto.gravaRotulo(rotuloEndereco, politicaSubstituicao, politicaEscrita, memoriaPrincipal,
                        endBinario)
                    leiturasNaMP += 1
                    encontrouNaMPLeitura += 1
            else:
                naoEncontrouNaCacheLeitura += 1
                conjunto = memoriaCache.gravaConjunto(enderecoConjunto)
                conjunto.gravaRotulo(rotuloEndereco, politicaSubstituicao, politicaEscrita, memoriaPrincipal,
                        endBinario)
                leiturasNaMP += 1
                encontrouNaMPLeitura += 1

        else:
            escritas += 1
            if politicaEscrita == 0: #Write Through
                conjunto = memoriaCache.procuraConjunto(enderecoConjunto)
                escritasNaCache += 1
                if not conjunto:
                    conjunto = memoriaCache.gravaConjunto(enderecoConjunto)
                    # conjunto.gravaRotulo(rotuloEndereco, politicaSubstituicao, politicaEscrita, memoriaPrincipal,
                    #     endBinario)
                    naoEncontrouNaCacheEscrita += 1
                else:
                    retornoRotulo = conjunto.procuraRotulo(rotuloEndereco)
                    if not retornoRotulo:
                        conjunto.gravaRotulo(rotuloEndereco, politicaSubstituicao, politicaEscrita, memoriaPrincipal,
                            endBinario)
                        naoEncontrouNaCacheEscrita += 1
                    else:
                        encontrouNaCacheEscrita += 1

                    escritasNaMP += 1
                    encontrouNaMPEscrita += 1
            else: #Write Back
                conjunto = memoriaCache.procuraConjunto(enderecoConjunto)
                escritasNaCache += 1
                if not conjunto:
                    conjunto = memoriaCache.gravaConjunto(enderecoConjunto)
                    conjunto.gravaRotulo(rotuloEndereco, politicaSubstituicao, politicaEscrita, memoriaPrincipal,
                        endBinario)
                    naoEncontrouNaCacheEscrita += 1
                else:
                    retornoRotulo = conjunto.procuraRotulo(rotuloEndereco)
                    if not retornoRotulo:
                        conjunto.gravaRotulo(rotuloEndereco, politicaSubstituicao, politicaEscrita, memoriaPrincipal,
                            endBinario)
                        naoEncontrouNaCacheEscrita += 1
                    else:
                        encontrouNaCacheEscrita += 1


    totalDeRegistros = leituras + escritas #Seta total de escritas;
    totalDeEscritas = escritas
    totalDeLeituras = leituras

    taxaDeAcertoCacheLeitura = 0
    #Acerto Leitura Cache
    if leiturasNaCache:
        taxaDeAcertoCacheLeitura = (encontrouNaCacheLeitura*100)/leiturasNaCache
        taxaDeErroCacheLeitura = (naoEncontrouNaCacheLeitura*100)/leiturasNaCache


    #Acerto Leitura MP
    if leiturasNaMP:
        taxaDeAcertoMPLeitura = (encontrouNaMPLeitura*100)/leiturasNaMP
        #Erro Leitura MP
        taxaDeErroMPLeitura = (naoEncontrouNaMPLeitura*100)/leiturasNaMP

    if escritasNaCache:
        #Erro Escrita Cache
        taxaDeErroCacheEscrita = (naoEncontrouNaCacheEscrita*100)/escritasNaCache
        #Acerto Escrita Cache
        taxaDeAcertoCacheEscrita = (encontrouNaCacheEscrita*100)/escritasNaCache

    # tempoAcesso = Integer.parseInt(acessoCache.getText());
    # tempoMP = Integer.parseInt(leituraMP.getText());

    if taxaDeAcertoCacheLeitura:
        tempoMedio = (((taxaDeAcertoCacheLeitura/100)*tempoAcesso) +
                ((1 - (taxaDeAcertoCacheLeitura/100)) * (tempoAcesso + tempoMP)))
        #Tm = h*tcache + (1-h) * (tcache + tMP)
    #h = taxa de acerto

    l1 = "Politica de Escrita: "+ str(politicaEscrita) + ", \n"
    l2 = "Tamanho da linha: "+ str(tamanhoDaLinha) + ", \n"
    l3 = "Numero de linhas: "+ str(numeroDeLinhas) + ", \n"
    l4 = "Assossiatividade por conjunto: "+ str(linhasPorConjunto) + ", \n"
    l5 = "Tempo de Acesso na Cache: "+ str(tempoAcesso) + ", \n"
    l6 = "Politica de Substituição: "+ str(politicaSubstituicao) + ", \n"
    l7 = "Tempo de Acesso na memória principal: "+ str(tempoMP) + ", \n"
    l8 = "Total de registros na cache: "+ str(totalDeRegistros) + ", \n"
    l9 = "Total de leituras na cache: "+ str(totalDeLeituras) + ", \n"
    l10 = "Total de escritas na cache: "+ str(totalDeEscritas) + ", \n"
    l11 = "Total de escritas na MP: " + ", \n"
    l12 = "Total de leituras na MP: "+ ", \n"
    l13 = "Taxa de acerto: "+ ", \n"
    l14 = "Tempo medio de acesso da cache: "+ ", \n"
    texto = l1+l2+l3+l4+l5+l6+l7+l8+l9+l10+l11+l12+l13+l14
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
