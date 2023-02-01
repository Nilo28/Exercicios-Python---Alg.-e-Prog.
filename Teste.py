#Escreva um programa que remova duplicados em um dicionário:
# Formato do Dicionário
# Dicionário = { Chave1 : { Item1 : [ Dado1, Dado2 ], Item2 : [ Dado1, Dado2 ]} 
#                Chave2 : { Item1 : [ Dado1, Dado2 ], Item2 : [ Dado1, Dado2 ]} 
#                Chave3 : { Item1 : [ Dado1, Dado2 ], Item2 : [ Dado1, Dado2 ]} 
#              }

import time
import os
os.system('cls || clear')

#Função Principal x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
def main():
    Dados = {  #Dicionário ---> #Prof1 = Prof5, Prof2 = Prof6,
    'Prof1' : { 'Nome' : ['José'], 'Disciplina' : ['Matemática', 'Geometria'] },
    'Prof2' : { 'Nome' : ['Maria'], 'Disciplina' : ['Inglês', 'Espanhol'] },
    'Prof3' : { 'Nome' : ['Juan'], 'Disciplina' : ['Matemática', 'Geometria'] },
    'Prof4' : { 'Nome' : ['Amanda'], 'Disciplina' : ['Inglês', 'Espanhol'] },
    'Prof5' : { 'Nome' : ['José'], 'Disciplina' : ['Matemática', 'Geometria'] }, 
    'Prof6' : { 'Nome' : ['Maria'], 'Disciplina' : ['Inglês', 'Espanhol'] } 
    }

    print("TABELA ORIGINAL ============")
    ImprimeDados(Dados)

    print("\nIdentificando os dados duplicados...")
    time.sleep(1)
    ChaveValorRepetido = IdentificaDadosRepetidos(Dados)
    
    print("\nDeletando os dados duplicados...")
    time.sleep(1)
    Dados = DeletaDadosIguais(ChaveValorRepetido, Dados)
    
    print("\nTABELA ALTERADA ============")
    ImprimeDados(Dados)
    

#Funções Auxilares x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

def IdentificaDadosRepetidos(Dados):    #-->Função para identificar os valores repetidos
    Chaves = list(Dados.keys())    #-->Lista que apresenta as chaves do dicionário
    Valores = list(Dados.values())    #-->Lista que apresenta os valores do dicionário
    ChaveValorRepetido = []    #-->Lista que armazena as chaves dos valores repetidos
    
    #Percorre e compara os valores do dicionario. Se for igual, salva a chave do valor repetido
    for a in range(0, len(Dados)):
        for b in range(a + 1, len(Dados)):
            if Valores[a] == Valores[b]:
                ChaveValorRepetido.append(Chaves[b])
    return ChaveValorRepetido



def DeletaDadosIguais(ChaveValorRepetido, Dados):    #-->Função para deletar os valores repetidos
    for a in ChaveValorRepetido:
        del Dados[a]
    return Dados


def ImprimeDados(Dados):    #-->Função para imprimir o dicionário
    for chave, valor in Dados.items():
        print(chave, valor, sep=' ')


main()