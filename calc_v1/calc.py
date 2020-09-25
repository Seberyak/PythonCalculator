import sys
import re

ERROR_MSG = "(Error: {})"


def check(args, arg):
    if args[0] == "+":
        return arg + float(args[1])
    elif args[0] == "-":
        return arg - float(args[1])
    elif args[0] == "*":
        return arg * float(args[1])
    elif args[0] == "/":
        return arg / float(args[1])


if __name__ == '__main__':
    answer = 0
    try:
        arguments = re.split(r'(\D)', sys.argv[1])

        for i in range(len(arguments)):
            if i == 0:
                answer = float(arguments[i])

            elif i % 2 == 0:
                answer = check(arguments[i - 1:i + 1], answer)
        answer = int(answer + 0.5)
        print(answer)

    except Exception as err:
        print(ERROR_MSG.format(err))
