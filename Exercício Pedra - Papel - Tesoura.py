#Escreva um programa que simula o jogo conhecido como “Pedra, Papel e Tesoura” de um(a) jogador(a) contra o(a) outro(a).

import os
os.system('cls || clear')

#Verificação do valores

print("Escolha um número correspondente à opção desejada")
print("\nOpções:")
print("-> Opção [1] - Tesoura")
print("-> Opção [2] - Papel")
print("-> Opção [3] - Pedra\n")
Jog1 =  int(input("\n[Jogador 1] Escolha uma opção: "))

if( Jog1 > 0 and Jog1 < 4 ):
    
    os.system('cls || clear')
    print("Escolha um número correspondente à opção desejada")
    print("\nOpções:")
    print("-> Opção [1] - Tesoura")
    print("-> Opção [2] - Papel")
    print("-> Opção [3] - Pedra\n")
    Jog2 =  int(input("\n[Jogador 2] Escolha uma opção: "))
    
    if( Jog2 > 0 and Jog2 < 4 ):
        os.system('cls || clear')
 
        #Verificação do ganhador
        if( Jog1 == 1):
            if( Jog2 == 1):
                print("\n\nJogador 1 escolheu Tesoura")
                print("Jogador 2 escolheu Tesoura")
                print("\nEmpate\n")
            
            elif( Jog2 == 2):
                print("\n\nJogador 1 escolheu Tesoura")
                print("Jogador 2 escolheu Papel")
                print("\nJogador 1 venceu\n") 
            
            elif( Jog2 == 3):
                print("\n\nJogador 1 escolheu Tesoura")
                print("Jogador 2 escolheu Pedra")
                print("\nJogador 2 venceu\n")           
        
        elif( Jog1 == 2):
            
            if( Jog2 == 1):
                 print("\n\nJogador 1 escolheu Papel")
                 print("Jogador 2 escolheu Tesoura")
                 print("\nJogador 2 venceu\n")
            
            elif( Jog2 == 2):
                print("\n\nJogador 1 escolheu Papel")
                print("Jogador 2 escolheu Papel")
                print("\nEmpate\n")  
            
            elif( Jog2 == 3):
                print("\n\nJogador 1 escolheu Papel")
                print("Jogador 2 escolheu Pedra")
                print("\nJogador 1 venceu\n")       
        
        elif( Jog1 == 3):
            
            if( Jog2 == 1):
                print("\n\nJogador 1 escolheu Pedra")
                print("Jogador 2 escolheu Tesoura")
                print("\nJogador 1 venceu\n")
            
            elif( Jog2 == 2):
                print("\n\nJogador 1 escolheu Pedra")
                print("Jogador 2 escolheu Papel")
                print("\nJogador 2 venceu\n")
            
            elif( Jog2 == 3):
                print("\n\nJogador 1 escolheu Pedra")
                print("Jogador 2 escolheu Pedra")
                print("\nEmpate\n")
   
    else:
            print("\n============== ERROR 404 ===============")
            print("Jogador 2 escolheu uma opção inexistente\n")

else:
    print("\n============== ERROR 404 ===============")  
    print("Jogador 1 escolheu uma opção inexistente\n")