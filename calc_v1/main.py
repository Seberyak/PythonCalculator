import sys
import re

ERROR_MSG = "(Error: {})"
GLOBAL_VARIABLE = 0


def check(args):
    if args[0] == "+":
        return GLOBAL_VARIABLE + float(args[1])
    elif args[0] == "-":
        return GLOBAL_VARIABLE - float(args[1])
    elif args[0] == "*":
        return GLOBAL_VARIABLE * float(args[1])
    elif args[0] == "/":
        return GLOBAL_VARIABLE / float(args[1])


if __name__ == '__main__':
    try:
        arguments = re.split(r'(\D)', sys.argv[1])

        for i in range(len(arguments)):
            if i == 0:
                GLOBAL_VARIABLE = float(arguments[i])

            elif i % 2 == 0:
                GLOBAL_VARIABLE = check(arguments[i-1:i+1])

        print(GLOBAL_VARIABLE)

    except Exception as err:
        print(ERROR_MSG.format(err))
