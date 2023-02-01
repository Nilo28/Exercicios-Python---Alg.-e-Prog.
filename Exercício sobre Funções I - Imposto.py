#Discente: Nilo Rodrigues Alves Filho
#Faça um programa com uma função chamada somaImposto. 
#A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem, e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

#Função Principal
def main():
    Custo = int(input("Digite o valor do item: "))
    TaxaImposto = int(input("Digite a porcentagem de imposto sobre o item: "))  
    Novo_Valor = SomaImposto(Custo, TaxaImposto)
    print(f"\nO valor final do produto é {Novo_Valor}.")


#Funções Auxiliares
def SomaImposto(Custo, TaxaImposto):    #Função que calcula o valor com imposto acrescido
    resultado = Custo + (Custo * TaxaImposto) / 100
    return resultado


main()