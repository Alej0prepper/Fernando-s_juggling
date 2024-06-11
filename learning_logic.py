import random
import re 

def subconjunto_aleatorio(cadena, k):
    caracteres = list(cadena)
    random.shuffle(caracteres)
    subconjunto = caracteres[:k]
    return ''.join(subconjunto)

def es_siteswap_valido(siteswap):
    digitos = [int(digito) for digito in siteswap]
    suma_digitos = sum(digitos)
    longitud_siteswap = len(digitos)
    return suma_digitos % longitud_siteswap == 0

def encontrar_mayor_numero(cadena):
    numeros = [i for i in cadena]
    numeros_enteros = [int(numero) for numero in numeros]
    return max(numeros_enteros) if numeros_enteros else None

def todos_pares(lista):
    for num in lista:
        if int(num) % 2!= 0:
            return False
    return True

def todos_impares(lista):
    for num in lista:
        if int(num) % 2 == 0:
            return False
    return True

def genera_secuencia_siteswaps(siteswap):
    if(todos_pares(siteswap)):
        aux = [0,2,4,6,8]
    elif(todos_impares(siteswap)):
        aux = [1,3,5,7,9]
    else: aux = [0,1,2,3,4,5,6,7,8,9]
    exit = []
    if(len(siteswap)>1):
        for i in aux:
            if(i <= encontrar_mayor_numero(siteswap)):
                exit.append(i)
    for i in range(len(siteswap)-2):
        end = False
        while(not end):
            aux = subconjunto_aleatorio(siteswap,i+2)
            if(es_siteswap_valido(aux)):
                end = True
        exit.append(aux)
    exit.append(siteswap)
    return exit
