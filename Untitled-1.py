#Discente: Nilo Rodrigues Alves Filho

#Escreva um programa que remova duplicados em um dicionário:

### Formato do Dicionário
#   Dicionário = { Chave1 : { Item1 : Valor1, Item2 : [ Valor1, Valor2 ]} 
#                  Chave2 : { Item1 : Valor1, Item2 : [ Valor1, Valor2 ]} 
#                  Chave3 : { Item1 : Valor1, Item2 : [ Valor1, Valor2 ]} 
#                }

### Dicionário Interno --> { Item1 : Valor1, Item2 : [ Valor1, Valor2 ]}

### Nota: *O programa lê apenas os valores, ignorando quaisquer chaves.
#         *Logo as Chaves(Item1, Item2, Item3...) entre os dicionários podem ser diferentes.
#         *Mesmo com chaves diferentes, se os valores associados forem iguais. A informação será deletada.
#          - Exemplo:
#            Dicionário = { Chave1 : { Nome : 'José', Disciplina : [ 'Algoritmos', 'Programação' ]} 
#                           Chave2 : { nome : 'Torres', disciplina : [ 'Algoritmos', 'Programação' ]} 
#                           Chave3 : { NOME : 'Torres', DISCIPLINA : [ 'Algoritmos', 'Programação' ]} 
#                         }
#                         Nome != nome != NOME      e      Disciplina != disciplina != DISCIPLINA
#                         Chave3 será deletada.
#         *Caso seja preciso verificar se as chaves(Item1, Item2, Item3,...) entre os dicionários internos são iguais:
#           - Ignorar a Função SeparaDuplicados() dentro da Função main()
#           - Enviar 'Dados' como parâmetro da Função IdentificaDuplicados() dentro da Função main()

import time
import os
os.system('cls || clear')

#Função Principal x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
def main():
    Dados = {  #Dicionário ---> #Prof1 = Prof3 = Prof5, Prof2 = Prof6,
    'Prof1' : { 'Nome' : ['José'], 'Disciplina' : ['Matemática', 'Geometria'] },
    'Prof2' : { 'Nome' : ['Maria'], 'Disciplina' : ['Inglês', 'Espanhol'] },
    'Prof3' : { 'Nome' : ['José'], 'Disciplina' : ['Matemática', 'Geometria'] },
    'Prof4' : { 'Nome' : ['Amanda'], 'Disciplina' : ['Inglês', 'Espanhol'] },
    'Prof5' : { 'Nome' : ['José'], 'Disciplina' : ['Matemática', 'Geometria'] }, 
    'Prof6' : { 'Nome' : ['Maria'], 'Disciplina' : ['Inglês', 'Espanhol'] } 
    }

    print("TABELA ORIGINAL ============")  #Apresenta os Dados antes da alteração
    Imprime(Dados)

    ValoresDicionarioInterno = SeparaDados(Dados)
    print(ValoresDicionarioInterno)

    print("\nIdentificando os dados duplicados...")
    time.sleep(1)
    ChaveValorRepetido = IdentificaDuplicados(ValoresDicionarioInterno)
    
    print("\nDeletando os dados duplicados...")
    time.sleep(1)
    Dados = DeletaDuplicados(ChaveValorRepetido, Dados)
    
    print("\nTABELA ALTERADA ============") #Apresenta os Dados após a alteração
    Imprime(Dados)
    

#Funções Auxilares x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

def SeparaDados(Dados):    #-->Função que retorna um dicionário com os valores dos dicionários internos
    ValoresChaveUnica = list()    #-->Lista que armazena temporariamente os valores de um único dicionário interno
    ValoresDicionarioInterno = dict()    #-->Dicionário que armazena os valores dos dicionarios internos associados à chaves ligadas a cada dicionario interno.
                                         #   Ex.:{ Chave1 : { Item1 : Valor1, Item2 : [ Valor1, Valor2 ] }
                                         #       { Chave1 : [ [Valor], [ Valor1, Valor2 ] ] }
    
    for a in Dados:
        for b in Dados[a]: 
            ValoresChaveUnica.append(Dados[a][b])     #Adiciona à lista os valores do dicionário interno
        ValoresDicionarioInterno[a] = ValoresChaveUnica      #Adiciona ao dicionário os valores dos dicionários internos associado à sua chave(Chave1, Chave2,Chave3,...)
        ValoresChaveUnica = []    #Limpa a lista para receber os valores do próximo dicionário interno
    return ValoresDicionarioInterno


def IdentificaDuplicados(Dados):    #-->Função para identificar os valores repetidos
    Chaves = list(Dados.keys())    #-->Lista que apresenta as chaves do dicionário
    Valores = list(Dados.values())    #-->Lista que apresenta os valores do dicionário
    ChaveValorRepetido = list()    #-->Lista que armazena as chaves dos valores repetidos
    
    #Percorre e compara os valores do dicionário. Se for igual, salva a chave do valor repetido
    for a in range(0, len(Dados)):
        for b in range(a + 1, len(Dados)):
            if Valores[a] == Valores[b]:
                if not Chaves[b] in ChaveValorRepetido:
                  ChaveValorRepetido.append(Chaves[b])
    return ChaveValorRepetido



def DeletaDuplicados(ChaveValorRepetido, Dados):    #-->Função para deletar os valores repetidos
    print("Duplicados ->", ChaveValorRepetido)
    for a in ChaveValorRepetido:
        del Dados[a]
    return Dados


def Imprime(Dados):    #-->Função para imprimir o dicionário de forma organizada
    for chave, valor in Dados.items():
        print(chave, valor, sep=" ")


main()