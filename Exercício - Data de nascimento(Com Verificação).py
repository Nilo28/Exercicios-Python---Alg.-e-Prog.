#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprime a data com o nome do mês por extenso
#[DD/MM/AAAA]
#[0123456678]

import os
os.system('cls || clear')

#Função Principal
def main():
    data = input("Digite a data de nascimento no formato [DD/MM/AAAA]: ")

#Funções Auxiliares
def VerfInicial(data):   #Verificação formato de data 
    while data[2] != "/" or data[5] != "/" :
        Erro('data')


def VerfAno(data):   #Verficação formato do ano
    Ano = True
    while Ano:
        try:
            AAAA = int(data[6:9])
            Ano = False
        except:
            Erro('AAAA')


def VerfMes(data):   #Verficação formato de meses
    Mes = True
    while Mes:
        try:
            MM = int(data[3:5])
            if Mes > 0 and Mes < 13 :
                Mes = False
            else:
                print("Mês inexistente")
                data = input("Digite a data de nascimento no formato [DD/MM/AAAA]: ")
        except:
            Erro('MM')


def VerfDias(data):   #Verficação formato de dias
    Dias = True
    while Dias:
        try:
            DD = int(data[0:2])
            Dias = False
        except:
            Erro('DD')

def Erro(a):   #Mensagem de erro
    print(f"Formato de {a} errado")
    data = input("Digite a data de nascimento no formato [DD/MM/AAAA]: ")

main()