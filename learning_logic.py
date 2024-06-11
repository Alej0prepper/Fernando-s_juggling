import random
import re 

def random_subset(string, k):
    characters = list(string)
    random.shuffle(characters)
    subset = characters[:k]
    return ''.join(subset)

def is_siteswap_valid(siteswap):
    digits = [int(digit) for digit in siteswap]
    sum_digits = sum(digits)
    length_siteswap = len(digits)
    return sum_digits % length_siteswap == 0

def find_largest_number(string):
    numbers = [i for i in string]
    integers = [int(number) for number in numbers]
    return max(integers) if integers else None

def all_even(numbers_list):
    for num in numbers_list:
        if int(num) % 2!= 0:
            return False
    return True

def all_odd(numbers_list):
    for num in numbers_list:
        if int(num) % 2 == 0:
            return False
    return True

def generate_siteswap_sequence(siteswap):
    if(all_even(siteswap)):
        aux = [0,2,4,6,8]
    elif(all_odd(siteswap)):
        aux = [1,3,5,7,9]
    else: aux = [0,1,2,3,4,5,6,7,8,9]
    result = []
    if(len(siteswap) > 1):
        for i in aux:
            if(i <= find_largest_number(siteswap)):
                result.append(i)
    for i in range(len(siteswap)-2):
        done = False
        while(not done):
            aux = random_subset(siteswap,i+2)
            if(is_siteswap_valid(aux)):
                done = True
        result.append(aux)
    result.append(siteswap)
    return result

print(generate_siteswap_sequence('123422'))