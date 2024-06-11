##Learning logic
import random
import re 
##
def subconjunto_aleatorio(cadena, k):
    # Convertir la cadena en una lista de caracteres
    caracteres = list(cadena)
    # Mezclar la lista de caracteres
    random.shuffle(caracteres)
    # Seleccionar los primeros k caracteres de la lista mezclada
    subconjunto = caracteres[:k]
    return ''.join(subconjunto)
    # Convertir la lista de subconjunto de vuelta a cadena

def es_siteswap_valido(siteswap):
    # Convertir el siteswap (cadena) en una lista de enteros
    digitos = [int(digito) for digito in siteswap]
    # Calcular la suma de todos los dígitos
    suma_digitos = sum(digitos)
    # Calcular la longitud del siteswap
    longitud_siteswap = len(digitos)
    # Verificar si la suma de los dígitos dividida por la longitud del siteswap es un número entero
    return suma_digitos % longitud_siteswap == 0

def encontrar_mayor_numero(cadena):
    # Encontrar todos los números en la cadena
        numeros = [i for i in cadena]
        # Convertir cada número encontrado a entero
        numeros_enteros = [int(numero) for numero in numeros]
        # Retornar el mayor número encontrado
        return max(numeros_enteros) if numeros_enteros else None

def todos_pares(lista):
    # Iterar sobre cada elemento en la lista
    for num in lista:
        # Comprobar si el número no es par
        if int(num) % 2!= 0:
            # Si encontramos un número impar, retornamos False
            return False
    # Si hemos llegado aquí, todos los números son pares
    return True
def todos_impares(lista):
    # Iterar sobre cada elemento en la lista
    for num in lista:
        # Comprobar si el número es par (para excluirlo, ya que estamos buscando impares)
        if int(num) % 2 == 0:
            # Si encontramos un número par, retornamos False
            return False
    # Si hemos llegado aquí, todos los números son impares
    return True
# Analizar el siteswap
def generate_siteswap_sequence(siteswap):
        if(todos_pares(siteswap)):
            aux = ['0','2','4','6','8']
        elif(todos_impares(siteswap)):
            aux = ['1','3','5','7','9']
        else: aux = ['0','2','4','6','8','1','3','5','7','9']
    #devuelve una lista de siteswaps pares de tamanno 1... len(siteswap) donde cada uno es subconjunto de siteswap
        exit = []
        if(len(siteswap)>1):
            for i in aux:
                if(int(i) <= encontrar_mayor_numero(siteswap)):
                    exit.append(i)
        for i in range(len(siteswap)-2):
            end = False
            while(not end):
                aux = subconjunto_aleatorio(siteswap,i+2)
                if(es_siteswap_valido(aux)):
                    end = True
            exit.append(aux)
        return exit
##

# print(encontrar_mayor_numero('12343294842356'))
# print(generate_siteswap_sequence('2422'))
# print(generate_siteswap_sequence('1379555'))
# print(generate_siteswap_sequence('12425'))

#crea la funcion main
#genera sevuencia de aprendizaje

# print(generate_siteswap_sequence('1379555'))