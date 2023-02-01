# Crie um programa receba do usuário as seguintes informações:
#  -O usuário poderá informar um ‘id’ e uma nova disciplina. 
#  -O programa deverá atualizar a disciplina daquele id pela disciplina informada pelo usuário

import time
#Função Principal

def main():
    Professor = {
        'id1': {'Nome': ['José'], 'Disciplina': ['Algoritmos', 'Programação', 'Introdução']},
        'id2': {'Nome': ['Rodrigues'], 'Disciplina': ['Calculo', 'Programação', 'Compiladores']},
        'id3': {'Nome': ['Torres'], 'Disciplina': ['IHC', 'Programação', 'Introdução']},
        'id4': {'Nome': ['Neto'], 'Disciplina': ['Banco de dados', 'Redes', 'Inteligência artificial']}
    }
    print("\nTABELA ATUAL ", "=" * 50)
    Imprime(Professor)
    print("=" * 65)

    AcessaDisciplinas(Professor)
    Resposta = Pergunta()
    
    if Resposta == 1:
        AdicionaDisciplinas(Professor)

    elif Resposta == 2:
        Id, ValorDisciplina = SubstituiDisciplinas(Professor)

    Professor = AlteraDados(Professor, Id, ValorDisciplina)

    print("\nTABELA ALTERADA ", "=" * 47)
    Imprime(Professor)
    print("=" * 65)


#Funções Auxiliares

def Pergunta():
    while(True):
        try:
            print(" ")
            print("Digite '1' para adicionar novas disciplinas")
            print("Digite '2' para substituir todas as disciplinas")
            Resposta = int(input("Digite aqui -> "))
            print(" ")
            return Resposta
        except:
            print("\n" + "=" * 19, "| Número Inválido |", "=" * 19, sep="\n")


def AdicionaDisciplinas(Professor):    #Função para Adicionar as Disciplinas
    ValorDisciplina = list()    #Lista das disciplinas
    Id = VerificaId(Professor)
    Disciplinas = AcessaDisciplinas(Professor, Id)

    D


def AcessaDisciplinas(Professor, Id):    
    Disciplinas_Temp = list()    #-->Lista que armazena temporariamente os valores de um único dicionário interno
    Disciplinas = list()  
    
    Professor[Id]['Disciplina'].append()
    return Disciplinas


def PedeDisciplinas():
    while(True):
        try:
            Num = int(input("Digite  -> "))
            print(" ")
            return Resposta
        except:
            print("\n" + "=" * 19, "| Número Inválido |", "=" * 19, sep="\n")

def SubstituiDisciplinas(Professor):    #Função para Substituir as Disciplinas
    ValorDisciplina = list()    #Lista das disciplinas

    Id = VerificaId(Professor)

    ValorDisciplina.append(input("Digite todas as disciplinas: "))

    Dados = Id.lower(), ValorDisciplina
    return Dados


def VerificaId(Professor):    #Função que verifica se a 'id' digitada existe
    while(True):
        Id = input("\nDigite a 'id' que será alterada: ")
        
        if Id.lower() in Professor.keys():
            return Id.lower()
        elif not Id in Professor.keys():        
            print("\n" + "=" * 17, "| 'id' inválida |", "=" * 17, sep="\n")


def AlteraDados(Professor, Id, ValorDisciplina):    #Função que atualiza o dicionário
    print("\nAlterando...")
    time.sleep(1)
    Professor[Id]['Disciplina'] = ValorDisciplina
    print("\nDisciplina alterada.")
    time.sleep(1)
    return Professor


def Imprime(Professor):    #Função para imprimir 'Professores' de forma organizada
    for Id, Informacoes in Professor.items():
        print(Id, "-" * 60,)
        for ChaveInfo, ValorInfo in Informacoes.items():
            print("   " + ChaveInfo, ValorInfo, sep=": ")


main()