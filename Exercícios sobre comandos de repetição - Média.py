#Escreva um programa que calcule a média de n valores.

Quantidade_de_valores = int(input("Informe a quantidade de valores para calcular a média: "))
print("\n")


#Verificação se o número é positivo
while(Quantidade_de_valores < 1):
    print("***** A quantidade de valores deve ser positiva *****\n")
    Quantidade_de_valores = int(input("Informe a quantidade de valores para calcular a média: "))
    print("\n")


#Definindo o valores
Lista_dos_valores = []  #Cria uma lista para guardar os valores
for a in range(1, Quantidade_de_valores + 1):  #Repete o comando n vezes
    Lista_dos_valores.append(int(input("Digite o " + str(a) + "º valor: ")))  #Guarda o valores na lista


#Soma dos valores da lista
Soma_dos_valores = 0
for b in Lista_dos_valores:  #Repete n vezes
    Soma_dos_valores = Soma_dos_valores + b  #Soma todos os valores


#Cálculo da média
Média_dos_valores = Soma_dos_valores / Quantidade_de_valores


#Tirar os [] da lista
sequência = ""
for n in range(0, Quantidade_de_valores):
    if n < Quantidade_de_valores - 2:
        sequência = sequência + str(Lista_dos_valores[n]) + ", "
    if n == Quantidade_de_valores - 2:
        sequência = sequência + str(Lista_dos_valores[n]) + " e "
    if n == Quantidade_de_valores - 1:
        sequência = sequência + str(Lista_dos_valores[n])


#Mensagem
print("\nA media de " + str(sequência) + "\né " + str(Média_dos_valores))