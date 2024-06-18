from class_operadores import Operadores

def somar():
    #Variaveis que recebem o valor das entradas !!
    Valor1 = float(input("Escolha O Valor 1: "))
    Valor2 = float(input("Escolha O Valor 2: "))
    numeros = Operadores(Valor1, Valor2)
    print(Operadores.soma(numeros))
    
while True:
    print("---------CALCULADORA--------")
    print("- [1]- Adição              -")
    print("- [2]- Subtração           -")
    print("- [3]- Divisao             -")
    print("- [4]- Multiplicacao       -")
    print("- [0]- Sair                -")
    print("----------------------------")

    opcao = input("Digite a opção desejada --> ")

    if opcao == "1":
        somar()
    elif opcao == "2":
        pass
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")