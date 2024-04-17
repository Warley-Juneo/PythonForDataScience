import sys


def main(*args):
    """
        This function takes a string as an argument and
        counts the number of upper and lower case letters,
        punctuation marks, spaces and digits in the string.

        Args:
            string (str): A string to be analyzed.

        Returns:
            None

        Raises:
            AssertionError: If more than one argument is provided.
    """

    string = ""

    try:
        if len(args) > 2:
            assert False, "more than one argument is provided"
        elif len(args) == 1:
            string = False
            while not string:
                string = input("")
        else:
            string = args[1]
    except AssertionError as e:
        print(e)
        return

    upper_letters, lower_letters, punctuation, spaces, digits = 0, 0, 0, 0, 0

    for i in range(0, len(string)):
        if string[i].isupper():
            upper_letters += 1
        elif string[i].islower():
            lower_letters += 1
        elif string[i].isspace():
            spaces += 1
        elif string[i].isdigit():
            digits += 1
        else:
            punctuation += 1

    total_characters = upper_letters + lower_letters \
        + punctuation + spaces + digits
    print(f"The text contains {total_characters} characters:\n{upper_letters} \
        upper letters\n{lower_letters} lower letters\n{punctuation} \
        punctuation marks\n{spaces} spaces\n{digits} digits")
    return


if __name__ == "__main__":
    main(*sys.argv)
