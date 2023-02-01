import random

L_Possibilidades = []    # --> Armazena todas as possibilidades
L_Aux = []     # --> Armazena temporariamente uma possibilidade
Bolinhas = 20     # --> Quantidade de números a serem sorteados
Tamanho = 3   # --> Quantidade de números de cada possibilidade

#Calculando o número de possibilidades
# -x- Combinação Simples -x-
Fatorial_A = 1  #(n)!
for a in range(Bolinhas, 0, -1):
    Fatorial_A = Fatorial_A * a
Fatorial_B = 1  #(n-p)!
for b in range(Bolinhas - Tamanho, 0, -1):
    Fatorial_B = Fatorial_B * b   
Fatorial_C = 1  #(p)!
for c in range(Tamanho, 0, -1):
    Fatorial_C = Fatorial_C * c
#C(n,p) = n!/[p!*(n-p)!]
Total_Possibilidades = Fatorial_A / (Fatorial_B * Fatorial_C)

#Sorteio e Armazenamento de todas as possibilidades
while len(L_Possibilidades) <= int(Total_Possibilidades):
    ##Sorteio
    cont = 1
    while cont < Tamanho + 1:
        Numero = random.randint(1,Bolinhas)
        Numero = '{:02d}'.format(Numero)
        if not Numero in L_Aux:
            L_Aux.append(Numero)
            cont += 1
    
    #Armazenamento
    L_Aux.sort()
    if not L_Aux in L_Possibilidades:
        L_Possibilidades.append(L_Aux)
        L_Aux = []
        cont = 1
    if len(L_Possibilidades) == Total_Possibilidades:
        break
    else:
        L_Aux = []
        cont = 1 

#Imprimindo as possibilidades
aux = ""  
x = 1
for n in range(0, int(Total_Possibilidades)):
    if x < 3:
        aux = aux + f"{'{:04d}'.format(n + 1)}º possiblidade: " + str(L_Possibilidades[n]) + "   |   "
        x += 1
    elif x == 3:
        aux = aux + f"{'{:04d}'.format(n + 1)}º possiblidade: " + str(L_Possibilidades[n])
        aux = aux + "\n"
        x = 1
print(aux)
print(f"Total de {len(L_Possibilidades)} possibilidades.")