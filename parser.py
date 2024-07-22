def parse_siteswap(siteswap_string):
    # Convierte la cadena de siteswap a una lista de enteros
    siteswap_numbers = [int(char) for char in siteswap_string]

    # Encuentra el número máximo en la lista para determinar el largo del array
    max_number = max(siteswap_numbers)

    # Calcula el promedio de los números en la lista
    average_number = sum(siteswap_numbers) / len(siteswap_numbers)

    # Determina el número de unos en el array (redondeando hacia abajo)
    num_ones = int(average_number)

    # Crea el array con los unos y los ceros necesarios
    result_array = [1] * num_ones + [0] * (max_number - num_ones)

    return result_array