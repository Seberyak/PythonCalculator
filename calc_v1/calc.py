import sys
import re

ERROR_MSG = "(Error: {})"


def check(args, arg):
    if args[0] == "+":
        return arg + float(args[1])
    if args[0] == "-":
        return arg - float(args[1])
    if args[0] == "*":
        return arg * float(args[1])
    if args[0] == "/":
        return arg / float(args[1])
    return None


if __name__ == '__main__':
    ANSWER = 0
    try:
        arguments = re.split(r'(\D)', sys.argv[1])

        for i, el in enumerate(arguments):
            if i == 0:
                ANSWER = float(arguments[i])

            elif i % 2 == 0:
                ANSWER = check(arguments[i - 1:i + 1], ANSWER)
        ANSWER = int(ANSWER + 0.5)
        print(ANSWER)

    except Exception as err:
        print(ERROR_MSG.format(err))
