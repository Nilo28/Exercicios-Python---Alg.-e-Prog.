#Tarefas sobre expressões ===============================================================================
#Escreva um programa que calcule a área de um retângulo. O usuário deve informar a altura e a largura.
#Escreva um programa que receba um valor em Celsius digitado pelo usuário, e converta em Farenheit.
#Escreva um programa que receba um valor em Farenheit digitado pelo usuário, e converta em Celsius.
#========================================================================================================




#===== Área do retângulo ================================================================================

print("\n\n===============  Área do retângulo ===============\n")

Altura = float(input("Digite o valor da altura do retângulo: "))
Largura =float(input("Digite o valor da largura do retângulo: "))

Area = Altura * Largura

print("\nA valor da área do retângulo é igual a", Area)


#========================================================================================================




#===== Conversão Celsius -> Farenheit ===================================================================

print("\n========= Conversão Celsius -> Farenheit =========\n")

Celsius1 = float(input("Digite o valor da temperatura em Celsius: "))

Farenheit1 = Celsius1 * 1.8 + 32

print("\nA temperatura de %.2f" %Celsius1, "°C é igual a %.2f" %Farenheit1, "°F")

#========================================================================================================




#===== Conversão Farenheit -> Celsius ===================================================================

print("\n========= Conversão Farenheit -> Celsius =========\n")

Farenheit2 = float(input("Digite o valor da temperatura em Farenheit: "))

Celsius2 = (5 * Farenheit2 - 160) / 9

print("\nA temperatura de %.2f" %Farenheit2, "°F é igual a %.2f" %Celsius2, "°C")
print("\n============== O programa finalizou ==============\n\n")

#========================================================================================================
