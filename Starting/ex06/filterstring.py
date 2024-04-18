import sys


def filter_words(string, length):
    """
    Filtra palavras de uma string que têm um comprimento maior que determinado
    comprimento.

    Args:
        string (str): A string a ser filtrada
        length (int): O comprimento a ser comparado

    Returns:
        List[str]: Uma lista de palavras da string que têm um comprimento
        maior que o comprimento dado.
    """

    return [word for word in string.split() if len(word) >= length]


def main(*args):
    """
        Função principal que chama a função filter_words e imprime o resultado.
    """

    try:
        if len(args) != 3:
            assert False, "the arguments are bad"
        string = args[1]
        if not all(char.isalpha() or char.isspace() for char in string):
            assert False, "the arguments is bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    try:
        length = int(args[2])
    except ValueError:
        print("AssertionError: the arguments is bad")
        return

    result = filter_words(string, length)
    print(result)

    return


if __name__ == "__main__":
    main(*sys.argv)
