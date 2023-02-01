#Prova 28/04/21

#Questão 4
#Pedir 2 números inteiros e 1 real 

#O produto do dobro do primeiro com metade do segundo

#Num1 = int(input("Digite um valor inteiro: "))
#Num2 = int(input("Digite um valor inteiro: "))
#Num3 = float(input("Digite um valor real: "))

#prod = ( 2 * Num1 ) * ( Num2 / 2 ) 

#print("\nO produto do dobro do primeiro com a metade do segundo é", prod)

#A soma do triplo do primeiro com o terceiro.

#Num1 = int(input("Digite um valor inteiro: "))
#Num2 = int(input("Digite um valor inteiro: "))
#Num3 = float(input("Digite um valor real: "))

#prod = ( 3 * Num1 ) + ( Num3 ) 

#print("\nA soma do triplo do primeiro com o terceiro é", prod)

#============================================================================

#Questão 5
#Escreva um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês

#ValorHora = float(input("Qual valor, em reais, você recebe por hora?\n"))
#NumHoras = float(input("Quantas horas você trabalha por mês?\n"))
 
#Salario = ValorHora * NumHoras

#print("Você recebe R$" + str(Salario) + " em um mês." )  

#============================================================================

#Questão 6
#Escreva um programa que receba do usuário os valores de um retângulo (da base e da altura). 
#Em seguida faça dois procedimentos: 
#i) calcule a área desse retângulo; 
#ii) em seguida mostre o dobro desta área para o usuário:

#Base = float(input("Digite o valor da base do retângulo: ")) 
#Altura = float(input("Digite o valor da altura do retângulo: "))

#Area = Base * Altura

#print("\nA área do retângulo é igual a ", Area)
#print("O dobro da área do retângulo é ", 2*Area)

#============================================================================

#Questão 7
#Escreva um programa Python que peça do usuário o raio de um círculo e calcule a área.

#Raio = float(input("Digite o valor do raio do círculo: "))

#Area = (Raio**2) * 3.14159

#print("\nO valor da área é %.2f" %Area)

#============================================================================

#Questão 8
#Faça um programa que leia como entrada o ano de nascimento da pessoa e imprima quantos anos ela fez em 2020

AnoNasc = int(input("Digite o ano de nascimento:"))

Idade2020 = 2020 - AnoNasc

print("\nEm 2020 você completou " + str(Idade2020) + " anos.")