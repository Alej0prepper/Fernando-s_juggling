def displaced_alphabet_index(letter):
    """
    Calculates the displaced index of a given letter in the alphabet.

    Args:
        letter (str): The letter for which the displaced index needs to be calculated.

    Returns:
        int: The displaced index of the letter.

    Raises:
        ValueError: If the input is not a single letter.

    Example:
        >>> displaced_alphabet_index('a')
        10
        >>> displaced_alphabet_index('z')
        35
    """
    
    if not isinstance(letter, str) or len(letter)!= 1:
        raise ValueError("Input must be a single letter.")
    
    lower_letter = letter.lower()  # Ensure the input is lowercase for consistency
    
    # Define the alphabet mapping
    alphabet_mapping = {
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17,
        'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25,
        'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33,
        'y': 34, 'z': 35
    }
    
    original_index = alphabet_mapping[lower_letter] 
    displaced_index = (original_index)  # Calculate the new index after displacement
    
    return displaced_index


def tokenize_string(input_string):
    """
    Tokenizes a string by converting each character into a list element.

    Args:
        input_string (str): The input string to be tokenized.

    Returns:
        list: A list of characters, where each character is a separate element.
    """
    return [char for char in input_string]


input_string = "Hello3world"
tokens = tokenize_string(input_string)
print(tokens)
final = []
for item in tokens:
    try:
        displaced_index = displaced_alphabet_index(item)
        final.append(displaced_index)
    except ValueError:
        pass  # Ignora el error y continúa con el siguiente elemento
print(final)