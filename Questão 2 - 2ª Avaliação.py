L_1 = []    # --> Lista de amigos do Usuário 1
L_2 = []    # --> Lista de amigos do Usuário 2
L_Iguais = []   # --> Lista de amigos em comum


#Coletando e armazenando os nomes do amigos
cont = 1
print("-x- Usuário 1 -x-")
while cont < 11:
    amig = input(f"Digite qual o nome do {cont}º amigo(a): ")
    L_1.append(amig)
    cont += 1

cont2 = 1
print("\n-x- Usuário 2 -x-")
while cont2 < 11:
    amig = input(f"Digite qual o nome do {cont2}º amigo(a): ")
    L_2.append(amig)
    cont2 += 1


#Comparando se há amigos iguais
x = 0
for a in L_1:
    for b in L_2:
        if a == b:
            L_Iguais.append(a)
            x += 1


#Imprimindo a conclusão na tela
if x == 0:
    print("\nOs usuários 1 e 2 não possuem amigos em comum.")
elif x == 1:
    print("\nOs usuários 1 e 2 possuem 1 amigo(a) em comum:")
    print(L_Iguais)
elif x > 1:
    print(f"\nOs usuários 1 e 2 possuem {x} amigos(as) em comum:")
    print(L_Iguais)
