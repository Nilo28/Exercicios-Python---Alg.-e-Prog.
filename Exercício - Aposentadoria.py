#Crie um programa que leia um caractere (‘M’ ou ‘F’), que representa o sexo de um indivíduo, e dois inteiros, que representam a idade e o tempo de contribuição. 
#O programa deverá então imprimir “Aposentável” se o indivíduo atenda uma das situações:
# É do sexo masculino, possui pelo menos 65 anos e pelo menos 10 anos de contribuição.
# É do sexo masculino, possui pelo menos 63 anos e pelo menos 15 anos de contribuição.
# É do sexo feminino, possui pelo menos 63 anos e pelo menos 10 anos de contribuição.
# É do sexo feminino, possui pelo menos 61 anos e pelo menos 15 anos de contribuição. 
#Caso contrário, o programa deverá imprimir “Não Aposentável”.

import time
import os

#Verificação sexo
Verificação_Sexo = True
 
##Looping infinito
while Verificação_Sexo:
    Sexo = input("\nDigite 'M' para Sexo Masculino ou 'F' para Sexo Feminino: ") #Pergunta o sexo
    if Sexo.upper() == 'M':  #Condicional Masculina
        Verificação_Sexo = False  #Saída do Looping

    elif Sexo.upper() == 'F':  #Condicional Feminina
        Verificação_Sexo = False  #Saída do Looping

    else:  #Mensagem padrão de erro
        os.system('cls || clear')  #Limpa tela
        print("\n404 ERROR -~-")  #Mensagem de erro genérica
        print("Sexo inválido")  #Mensagem de erro genérica
        time.sleep(1)  #Espera 1 segundo
        os.system('cls || clear')  #Limpa tela


#Limpa a tela
time.sleep(1)
os.system('cls || clear')


#Verificação Tempo de Contribuição-Idade
Verificação_Tempo_Idade = True

##Looping infinito
while Verificação_Tempo_Idade:
    Idade = int(input("Digite sua idade em anos: "))  #Pergunta a idade
    Tempo_Contribuição = int(input("Digite seu tempo de contribuição em anos: "))  #Pergunta o tempo de contribuição
    if Tempo_Contribuição > Idade:  #Condicional ->A idade deve ser maior que o tempo de contribuição
        os.system('cls || clear')  #Limpa a tela
        print("\n404 ERROR -~-~-~-~-~-~-~-~-~-~-~-~-~-~-")  #Mensagem de erro genérica
        print("Tempo de contribuição maior que a idade")  #Mensagem de erro genérica
        time.sleep(2)  #Espera 2 segundos
        os.system('cls || clear')  #Limpa tela

    else:
        Verificação_Tempo_Idade = False  #Saída do Looping


#Limpa a tela
time.sleep(1)
os.system('cls || clear')


#Verficação Aposentadoria
if Sexo.upper() == 'M':  #Condicional -> Sexo Masculino
    if Idade >= 65 and Tempo_Contribuição >= 10:  #1ª condição de aposentadoria
        print("Sexo: Masculino")  #Imprime o sexo
        print("Idade: " + str(Idade) + " anos.")  #Imprime a idade
        print("Tempo de Contruibuição: " + str(Tempo_Contribuição) + " anos.")  #Imprime o tempo de contribuição
        print("\nStatus: Aposentável")  #Imprime o status do usuário

    elif Idade >= 63 and Tempo_Contribuição >= 15:  #2ª condição de aposentadoria
        print("Sexo: Masculino")  #Imprime o sexo
        print("Idade: " + str(Idade) + " anos.")  #Imprime a idade
        print("Tempo de Contruibuição: " + str(Tempo_Contribuição) + " anos.")  #Imprime o tempo de contribuição
        print("\nStatus: Aposentável")  #Imprime o status do usuário

    else:
        print("Sexo: Masculino")  #Imprime o sexo
        print("Idade: " + str(Idade) + " anos.")  #Imprime a idade
        print("Tempo de Contruibuição: " + str(Tempo_Contribuição) + " anos.")  #Imprime o tempo de contribuição
        print("\nStatus: Não Aposentável")  #Imprime o status do usuário

elif Sexo.upper() == 'F':  #Condicional -> Sexo Feminino
    if Idade >= 63 and Tempo_Contribuição >= 10:  #1ª condição de aposentadoria
        print("Sexo: Feminino")  #Imprime o sexo
        print("Idade: " + str(Idade) + " anos.")  #Imprime a idade
        print("Tempo de Contruibuição: " + str(Tempo_Contribuição) + " anos.")  #Imprime o tempo de contribuição
        print("\nStatus: Aposentável")  #Imprime o status do usuário

    elif Idade >= 61 and Tempo_Contribuição >= 15:  #2ª condição de aposentadoria
        print("Sexo: Feminino")  #Imprime o sexo
        print("Idade: " + str(Idade) + " anos.")  #Imprime a idade
        print("Tempo de Contruibuição: " + str(Tempo_Contribuição) + " anos.")  #Imprime o tempo de contribuição
        print("\nStatus: Aposentável")  #Imprime o status do usuário

    else:
        print("Sexo: Feminino")  #Imprime o sexo
        print("Idade: " + str(Idade) + " anos.")  #Imprime a idade
        print("Tempo de Contruibuição: " + str(Tempo_Contribuição) + " anos.")  #Imprime o tempo de contribuição
        print("\nStatus: Não Aposentável")  #Imprime o status do usuário
