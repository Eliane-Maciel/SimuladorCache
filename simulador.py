# -*- coding: utf-8 -*-
from memoria_cache import Linha, Conjunto, MemoriaCache, MemoriaPrincipal
from leitura_arquivo import leituraArquivo


def gravaDados():
    politica_escrita = int(raw_input('Politica de Escrita : 0 - write-through; 1 - write-back; '))
    tam_linha = int(raw_input('Tamanho da Linha : '))
    num_linhas = int(raw_input('Número de linhas: '))
    assossiatividade = int(raw_input('Assossiatividade por conjunto: '))
    tempo_acesso = int(raw_input('Tempo de acesso quando encontra (hit-time): '))
    politica_substituicao = int(raw_input('Politica de Substituição: 1 - LFU; 2 - LRU'))

    tempo_mp = int(raw_input('Tempo de leitura/escrita:'))
    enderecos = leituraArquivo()

    import ipdb; ipdb.set_trace()
    for end in enderecos:
        conjunto = num_linhas/assossiatividade
        tam_rotulo = 32 - (conjunto+5)


def main():
    gravaDados()


if __name__ == '__main__':
    main()
