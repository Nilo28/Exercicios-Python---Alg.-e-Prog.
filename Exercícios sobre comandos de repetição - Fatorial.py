#Escreva um programa que calcule o fatorial de um número.

Numero = int(input("Digite o valor de um número natural: "))


#Verificação da condição para calcular o Fatorial
while(Numero < 0):
    print("\n***** O Conjunto dos números naturais é composto números inteiros não-negativos *****\n")
    Numero = int(input("Digite o valor de um número NATURAL: "))


#Fatorial de 0
if Numero == 0:
    print("\nO fatorial de 0 é 1")


#Fatorial de um número maior que 0
elif Numero > 0:
    Fatorial = 1
    for a in range(Numero, 0, -1):
        Fatorial = Fatorial * a
    
    print("\nO fatorial de " + str(Numero) + " é", Fatorial)