def is_even(num):
    return num % 2 == 0

def is_positive(num):
    return num > 0

def is_vowel(char):
    return char.lower() in 'aeiou'

def is_none(item):
    return item is None

def is_string(item):
    return isinstance(item, str)
    
def ft_filter(function, iterable):
    """
    Implementation of the filter() function using list comprehension

    Args:
        function (callable): The function to be applied to the elements of the iterable
        iterable (list): The iterable to be filtered

    Returns:
        List: A new list with the elements that satisfy the condition
    """
    
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item

if __name__ == "__main__":
    print("Resultado da função \033[91mfilter()\033[0m em vermelho e da função \033[92mft_filter()\033[0m em verde:")

    # Teste 1: Números pares em uma lista
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter(is_even, iterable)
    result1 = ft_filter(is_even, iterable)
    print(f"\033[91m{list(result)}\033[0m")
    print(f"\033[92m{list(result1)}\033[0m")
    print()

    # Teste 2: Números positivos em uma lista
    iterable = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    result = filter(is_positive, iterable)
    result1 = ft_filter(is_positive, iterable)
    print(f"\033[91m{list(result)}\033[0m")
    print(f"\033[92m{list(result1)}\033[0m")
    print()

    # Teste 3: Vogais em uma string
    iterable = "Hello, World!"
    result = filter(is_vowel, iterable)
    result1 = ft_filter(is_vowel, iterable)
    print(f"\033[91m{list(result)}\033[0m")
    print(f"\033[92m{list(result1)}\033[0m")
    print()
    
    # Teste 4: Valores None em uma lista
    iterable = [None, 1, None, 2, None, 3, None, 4, None, 5]
    result = filter(is_none, iterable)
    result1 = ft_filter(is_none, iterable)
    print(f"\033[91m{list(result)}\033[0m")
    print(f"\033[92m{list(result1)}\033[0m")
    print()

    # Teste 5: Strings em uma lista mista
    iterable = ["Hello", 1, "World", 2, None, 3, "!", 4, None, 5]
    result = filter(is_string, iterable)
    result1 = ft_filter(is_string, iterable)
    print(f"\033[91m{list(result)}\033[0m")
    print(f"\033[92m{list(result1)}\033[0m")
    print()

    # Teste 6: Função None com uma lista
    iterable = [1, 2, 3, 4, 5]
    result = filter(None, iterable)
    result1 = ft_filter(None, iterable)
    print(f"\033[91m{list(result)}\033[0m")
    print(f"\033[92m{list(result1)}\033[0m")
    print()

    # Teste 7: Função com um iterável None
    try:
        result = filter(is_even, None)
        result1 = ft_filter(is_even, None)
        print(f"\033[91m{list(result)}\033[0m")
        print(f"\033[92m{list(result1)}\033[0m")
    except TypeError as e:
        print(f"\033[91m{e}\033[0m")
        print(f"\033[92m{e}\033[0m")
