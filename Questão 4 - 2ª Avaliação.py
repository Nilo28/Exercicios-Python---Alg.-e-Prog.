#Lista que armazena as perguntas
L_Perguntas = ["Telefonou para a vítima",
"Esteve no local do crime?", 
"Mora perto da vítima?", 
"Devia para a vítima?", 
"Já trabalhou com a vítima?"]

#Lista que armazena as respostas
L_Respostas = []


#Interrogatório
for a in range(0, len(L_Perguntas)):
    print(L_Perguntas[a])
    resposta = input("Digite 'sim' ou 'não' para responder a pergunta: ")
    print(" ")
    L_Respostas.append(resposta.upper())


#Veredito
cont = 0
for b in L_Respostas:
    if b == 'SIM':
        cont += 1

if cont == 2:
    print("Suspeito")
elif 3 <= cont <= 4:
    print("Cúmplice")
elif cont == 5:
    print("Assassino")
else:
    print("Inocente")
