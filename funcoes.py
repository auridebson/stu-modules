vogais = ["a","e","i","o","u","á","é","í","ó","ú","à"]

def pass_upper(texto:str):
    return texto.upper()

def pass_lower(texto:str):
    return texto.lower()

def conta_vogais(texto:str):
    controle = 0
    for letra in texto:
        if letra in vogais:
            controle = controle + 1
    return controle

def conta_consoantes(texto:str):
    controle = 0
    for letra in texto:
        if letra in vogais:
            continue
        else:
            controle = controle + 1
    return controle

def conta_caracteres(texto:str):
    controle = 0
    for letra in texto:
        controle = controle + 1
    return controle

def conta_palavras(texto:str):
    controle = 0
    for letra in texto:
        if letra == " ":
            controle = controle + 1
    return controle+1

def ln(x):
    print("-"*x)


def soma(num1:int, num2:int):
    resultado = num1 + num2
    return resultado

def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado

def divisao(num1,num2):
    resultado = num1 / num2
    return resultado

def multiplicacao(num1, num2):
    resultado = num1 * num2
    return resultado