from funcoes import *

ln(30)



while True:
    menu = int(input("""
    Escolha a operação que deseja fazer:
        [1] - Somar
        [2] - Subtrair
        [3] - Dividir
        [4] - Multiplicar
        [0] - Sair
    """))
    match menu:
        case 1:
            ln(10)
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            ln(15)
            print(f"Resultado: {soma(num1, num2)}")
            ln(15)
        case 2:
            print("Subtração escolhida")
        case 3:
            print("Divisão escolhida")
        case 4:
            print("Multiplicação escolhida")
        case 0:
            print("Saindo...")
            break