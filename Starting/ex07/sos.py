import sys


def main(*args):
    NESTED_MORSE = {
        " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ",
        "H": ".... ", "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ",
        "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ",
        "X": "-..- ", "Y": "-.-- ", "Z": "--.. ", "0": "----- ",
        "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ",
        "7": "--... ", "8": "---.. ", "9": "----. "
    }

    try:
        if len(args) != 2:
            assert False, "the arguments are bad"

        str1 = args[1].upper()
        if not all(char.isalnum() or char.isspace() for char in str1):
            assert False, "the arguments is bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    result = ""
    for char in str1:
        result += NESTED_MORSE[char]

    print(result)
    return


if __name__ == "__main__":
    main(*sys.argv)
