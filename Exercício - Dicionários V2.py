#Escreva um programa que remova duplicados em um dicionário:
# Formato do Dicionário
# Dicionário = { Chave1 : { Item1 : [ Dado1, Dado2 ], Item2 : [ Dado1, Dado2 ]} 
#                Chave2 : { Item1 : [ Dado1, Dado2 ], Item2 : [ Dado1, Dado2 ]} 
#                Chave3 : { Item1 : [ Dado1, Dado2 ], Item2 : [ Dado1, Dado2 ]} 
#              }

import time
import os
os.system("cls || clear")

######Função Principal
def main():
    Dados = ColetaDados()

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
    

######Funções Auxilares

def ColetaDados():    #-->Função para coletar os valores e chaves
    Dados = {}
    QuantidadeDados = int(input("Digite a quantidade de dados a serem armazenados: "))
    print("**** Cada informação deve ser associado à uma chave ****")
    
    print("=" * 30)
    while len(Dados) < QuantidadeDados:
        Chave = input(f"Digite a chave: ")
        Chave = VerificaChave(Chave, Dados)
        Valor = input(f"Digite a informação: ")
        Dados[Chave] = Valor
        print("Informação salva")
        print("\n" + "=" * 30)
    
    return Dados


def VerificaChave(Chave,Dados):    #-->Função para verificar se a chave já existe
    if Chave in Dados.keys():
        print("  |" + "-" * 60)
        print("  |Essa chave já existe")
        print("  |Digite '1' para permanecer a chave e alterar sua informação.")
        print("  |Digite '2' para alterar a chave.")
        a = int(input("  |Digite aqui: "))
        print("  |" + "-" * 60)
        if a == 2:
            Chave = input(f"Digite a chave: ")
            Chave = VerificaChave(Chave, Dados)
    return Chave


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
    for Chave, Valor in Dados.items():
        print(Chave, Valor, sep=" ")


main()