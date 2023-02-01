#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25],  [26-50], [51-75] e [76-100].
#A entrada de dados deverá terminar quando for lido um número negativo.

import os
import time

L_0_25 = [] #Intervalo [0-25]
L_26_50 = [] #Intervalo [26-50]
L_51_75 = [] #Intervalo [51-75]
L_76_100 = [] #Intervalo [76-100]

aux1 = True
while aux1:
    Valor = float(input("Digite um valor: "))
    if Valor < 0:
        print("\nValor negativo")
        print("\nFinalizando a contagem...")
        aux1 = False
    elif Valor > -1 and Valor < 26:
        L_0_25.append(Valor)
    elif Valor > 25 and Valor < 51:
        L_26_50.append(Valor)
    elif Valor > 50 and Valor < 76:
        L_51_75.append(Valor)
    elif Valor > 75 and Valor < 101:
        L_76_100.append(Valor)
    if Valor > -1:
        print("\n**Contagem de números**")
        print("Intervalo [0-25]: ", len(L_0_25))
        print("Intervalo [26-50]: ", len(L_26_50))
        print("Intervalo [51-75]: ", len(L_51_75))
        print("Intervalo [76-100]: ", len(L_76_100))
        time.sleep(1)
        os.system('cls || clear')

time.sleep(1)
os.system('cls || clear')
print("*" * 30) 
print("**Contagem final dos números**")
print("\nIntervalo [0-25]: ", len(L_0_25))
print("    ",L_0_25)
print("\nIntervalo [26-50]: ", len(L_26_50))
print("    ",L_26_50)
print("\nIntervalo [51-75]: ", len(L_51_75))
print("    ",L_51_75)
print("\nIntervalo [76-100]: ", len(L_76_100))
print("    ",L_76_100)
print("*" * 30)