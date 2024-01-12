from funcoes import *

ln(30)



# while True:
#     menu = int(input("""
#     Escolha a operação que deseja fazer:
#         [1] - Somar
#         [2] - Subtrair
#         [3] - Dividir
#         [4] - Multiplicar
#         [0] - Sair
#     """))

#     num1 = int(input("Digite o primeiro número: "))
#     num2 = int(input("Digite o segundo número: "))
#     match menu:
#         case 1:
#             ln(15)
#             print(f"Resultado: {soma(num1, num2)}")
#             ln(15)
#         case 2:
#             ln(15)
#             print(f"Resultado: {subtracao(num1, num2)}")
#             ln(15)
#         case 3:
#             ln(15)
#             print(f"Resultado: {divisao(num1, num2)}")
#             ln(15)
#         case 4:
#             ln(15)
#             print(f"Resultado: {multiplicacao(num1, num2)}")
#             ln(15)
#         case 0:
#             print("Saindo...")
#             break



while True:
    frase = input("Digite a primeira frase: ")
    print(vpalidromo(frase))
    menu = input("Deseja fazer outra verificação[s]/[n]: ")
    if menu.lower() == "n":
        break