import sys


def main(*args):
    if len(args) == 2:
        num_str = args[1]
        if num_str.startswith('-') \
                and num_str[1:].isdigit() or num_str.isdigit():
            num = abs(int(num_str))
            if num % 2 == 0:
                print("even")
            else:
                print("odd")
        else:
            print("AssertionError: argument is not an integer")
    elif len(args) > 2:
        print("AssertionError: more than one argument is provided")
    return


if __name__ == "__main__":
    main(*sys.argv)
