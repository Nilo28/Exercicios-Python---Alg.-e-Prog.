# Crie um programa receba do usuário as seguintes informações:
#  -O usuário poderá informar um ‘id’ e uma nova disciplina. 
#  -O programa deverá atualizar a disciplina daquele id pela disciplina informada pelo usuário

import time

#Função Principal

def main():
    Professor = {
        'id1': {'Nome': ['José'], 'Disciplina': ['algoritmos, programação, introdução']},
        'id2': {'Nome': ['Rodrigues'], 'Disciplina': ['calculo, programação, compiladores']},
        'id3': {'Nome': ['Torres'], 'Disciplina': ['IHC, programação, introdução']},
        'id4': {'Nome': ['Neto'], 'Disciplina': ['banco de dados, redes, inteligência artificial']}
    }
    print("\nTABELA ATUAL ", "=" * 50)
    Imprime(Professor)
    print("=" * 65)

    Id, ValorDisciplina = ColetaDados(Professor)

    Professor = AlteraDados(Professor, Id, ValorDisciplina)

    print("\nTABELA ALTERADA ", "=" * 47)
    Imprime(Professor)
    print("=" * 65)


#Funções Auxiliares

def ColetaDados(Professor):    #Função para coletar a 'id' que será alterada e a nova disciplina
    ValorDisciplina = list()    #Lista das disciplinas

    Id = ColetaVerificaId(Professor)
    print("AVISO: As disciplinas digitadas substituirão as disciplinas cadastradas")
    ValorDisciplina.append(input("Digite as disciplinas: "))

    Dados = Id.lower(), ValorDisciplina
    return Dados


def ColetaVerificaId(Professor):    #Função que verifica se a 'id' digitada existe
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