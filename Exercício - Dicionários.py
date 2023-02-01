#Discente: Nilo Rodrigues Alves Filho

#Escreva um programa que remova duplicados em um dicionário:

### Formato do Dicionário
#   Dicionário = { Chave1 : { Item1 : Valor1, Item2 : [ Valor1, Valor2, Valor3 ]} 
#                  Chave2 : { Item1 : Valor1, Item2 : [ Valor1, Valor2, Valor3 ]} 
#                  Chave3 : { Item1 : Valor1, Item2 : [ Valor1, Valor2, Valor3 ]} 
#                }

### Dicionário Interno --> { Item1 : Valor1, Item2 : [ Valor1, Valor2, Valor3 ]}

### Nota: *O programa lê apenas os valores, ignorando quaisquer chaves.
#         *Logo as Chaves(Item1, Item2...) entre os dicionários podem ser diferentes.
#         *Mesmo com chaves diferentes, se os valores associados forem iguais. A informação será deletada.
#          - Exemplo:
#            Dicionário = { Chave1 : { Nome : 'José', Disciplina : [ 'Algoritmos', 'Programação', 'Introdução' ]} 
#                           Chave2 : { nome : 'Torres', disciplina : [ 'Calculo', 'Programação', 'Compiladores' ]} 
#                           Chave3 : { NOME : 'José', DISCIPLINA : [ 'Algoritmos', 'Programação', 'Introdução' ]} 
#                         }
#                         Nome != nome != NOME      e      Disciplina != disciplina != DISCIPLINA
#                         Chave3 será deletada.
#         *Caso seja preciso verificar se as chaves(Item1, Item2...) entre os dicionários internos são iguais:
#           - Ignorar a Função 'SeparaDados()' dentro da Função 'main()'
#           - Enviar 'Dados' como parâmetro da Função 'IdentificaDuplicados()' dentro da Função 'main()'
import time
import os

#Função Principal

def main():
    Dados = {
        'id1': {'Nome': ['José'], 'Disciplina': ['Algoritmos', 'Programação', 'Introdução']},
        'id2': {'Nome': ['Torres'], 'Disciplina': ['Calculo', 'Programação', 'Compiladores']},
        'id3': {'Nome': ['José'], 'Disciplina': ['Algoritmos', 'Programação', 'Introdução']},
        }

    print("TABELA ORIGINAL " + "=" * 68)  #Apresenta 'Dados' antes da alteração
    Imprime(Dados)
    print("=" * 84)
    time.sleep(1)

    ValoresDicionarioInterno = SeparaDados(Dados)

    print("\nIdentificando os dados duplicados...")
    time.sleep(1)
    ChaveValorRepetido = IdentificaDuplicados(ValoresDicionarioInterno)
    print("Duplicados ->", ChaveValorRepetido)
    
    print("\nDeletando os dados duplicados...")
    time.sleep(1)
    Dados = DeletaDuplicados(ChaveValorRepetido, Dados)
    
    print("\nTABELA ALTERADA " + "=" * 68) #Apresenta 'Dados' após a alteração
    Imprime(Dados)
    print("=" * 84)
    

#Funções Auxilares

def SeparaDados(Dados):    #-->Função que retorna um dicionário com os valores dos dicionários internos
    ValoresChaveUnica = list()    #-->Lista que armazena temporariamente os valores de um único dicionário interno
    ValoresDicionarioInterno = dict()    #-->Dicionário que armazena os valores dos dicionarios internos associados à chaves ligadas a cada dicionario interno.
                                         #   Ex.:{ Chave1 : { Item1 : Valor1, Item2 : [ Valor1, Valor2, Valor3 ] }
                                         #       { Chave1 : [ [Valor], [ Valor1, Valor2, Valor3 ] ] }
    
    for a in Dados:
        for b in Dados[a]: 
            ValoresChaveUnica.append(Dados[a][b])     #Adiciona à lista os valores do dicionário interno
        ValoresDicionarioInterno[a] = ValoresChaveUnica      #Adiciona ao dicionário os valores dos dicionários internos associado à sua chave(Chave1, Chave2,Chave3,...)
        ValoresChaveUnica = []    #Limpa a lista para receber os valores do próximo dicionário interno
    return ValoresDicionarioInterno


def IdentificaDuplicados(Dicionario):    #-->Função para identificar os valores repetidos de um dicionario
    Chaves = list(Dicionario.keys())    #-->Lista que apresenta as chaves de um dicionário
    Valores = list(Dicionario.values())    #-->Lista que apresenta os valores de um dicionário
    ChaveValorRepetido = list()    #-->Lista que armazena as chaves dos valores repetidos
    
    #Percorre e compara os valores do dicionário. Se for igual, salva a chave do valor repetido em uma lista
    for a in range(0, len(Dicionario)):
        for b in range(a + 1, len(Dicionario)):
            if Valores[a] == Valores[b]:
                if not Chaves[b] in ChaveValorRepetido:
                  ChaveValorRepetido.append(Chaves[b])

    return ChaveValorRepetido



def DeletaDuplicados(ChaveValorRepetido, Dicionario):    #-->Função para deletar os valores repetidos de um dicionario
    for a in ChaveValorRepetido:
        del Dicionario[a]
    return Dicionario


def Imprime(Dicionario):    #-->Função para imprimir o dicionário de forma organizada
    for chave, valor in Dicionario.items():
        print(chave, valor, sep=" ")


main()