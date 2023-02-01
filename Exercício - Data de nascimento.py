#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprime a data com o nome do mês por extenso
#[DD/MM/AAAA]
#[0123456678]


import os
os.system('cls || clear')

data = input("Digite a data de nascimento no formato [DD/MM/AAAA]: ")

#Verificação da data
V1 = V2 = V3 = V4 = True
while V1 or V2 or V3 or V4 :
    #Formato DD/MM/AAAA
    if data[2] != "/" or data[5] != "/" :
        print("Formato de data errado")
        data = input("Digite a data de nascimento no formato [DD/MM/AAAA]: ")
    else :
        V1 = False

    #ANO
    Ano = True
    while Ano :
        try :
            AAAA = int(data[6:9])
            Ano = False
            V2 = False
        except :
            print("Formato de AAAA errado")
            data = input("Digite a data de nascimento no formato [DD/MM/AAAA]: ")

    #MES
    Mes = True
    while Mes :
        try :
            MM = int(data[3:5])
            if Mes > 0 and Mes < 13 :
                Mes = False
                V3 = False
            else :
                print("Mês inexistente")
                data = input("Digite a data de nascimento no formato [DD/MM/AAAA]: ")
        except :
            print("Formato de MM errado")
            data = input("Digite a data de nascimento no formato [DD/MM/AAAA]: ")

    #DIA
    Dias = True
    while Dias :
        try :
            DD = int(data[0:2])
            Dias = False
            V4 = False
        except :
            print("Formato de DD errado")
            data = input("Digite a data de nascimento no formato [DD/MM/AAAA]: ")
