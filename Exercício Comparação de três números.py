#Escreva um programa que lê três números distintos e os imprime em ordem decrescente

import os
os.system('cls || clear')

print("Digite 3 números distintos")
Num1 = int(input("Digite o 1º número: "))
Num2 = int(input("Digite o 2º número: "))
Num3 = int(input("Digite o 3º número: "))

#Verificação dos números
if(Num1 == Num2 or Num2 == Num3 or Num1 == Num3):
    print("\n========== ERROR 404 =========")
    print("Foram digitados números iguais")

#Comparação dos valores
elif((Num1 > Num2 and Num1 > Num3) and Num2 > Num3):
    print(str(Num1) + " > " + str(Num2) + " > " + str(Num3))

elif((Num1 > Num2 and Num1 > Num3) and Num2 < Num3):        
    print(str(Num1) + " > " + str(Num3) + " > " + str(Num2))

elif((Num2 > Num1 and Num2 > Num3) and Num1 > Num3):
    print(str(Num2) + " > " + str(Num1) + " > " + str(Num3))

elif((Num2 > Num1 and Num2 > Num3) and Num3 > Num1):
    print(str(Num2) + " > " + str(Num3) + " > " + str(Num1))
        
elif((Num3 > Num1 and Num3 > Num2) and Num1 > Num2):
    print(str(Num3) + " > " + str(Num1) + " > " + str(Num2))

elif((Num3 > Num1 and Num3 > Num2) and Num2 > Num3):
    print(str(Num3) + " > " + str(Num2) + " > " + str(Num1))