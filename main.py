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



entrada = pass_lower(input("Digite o seu texto: "))


print(conta_caracteres(entrada))