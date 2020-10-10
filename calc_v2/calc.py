import sys
import re

ERROR_MSG = "(Error: {})"


def ordering_operations(args):
    if '*' in args:
        operand_position = args.index('*')
        args = args[:operand_position - 1] + [
            calculate(args[operand_position - 1], args[operand_position], args[operand_position + 1])] + args[
                                                                                                         operand_position + 2:]

    elif "/" in args:
        operand_position = args.index('/')
        args = args[:operand_position - 1] + [
            calculate(args[operand_position - 1], args[operand_position], args[operand_position + 1])] + args[
                                                                                                         operand_position + 2:]
    else:
        operand_position = 1
        args = args[:operand_position - 1] + [
            calculate(args[operand_position - 1], args[operand_position], args[operand_position + 1])] + args[
                                                                                                         operand_position + 2:]

    if len(args) > 1:
        return ordering_operations(args)

    return args[0]


def calculate(var_1, operand, var_2):
    res = 0
    if operand == "+":
        res = float(var_1) + float(var_2)
    if operand == "-":
        res = float(var_1) - float(var_2)
    if operand == "*":
        res = float(var_1) * float(var_2)
    if operand == "/":
        res = float(var_1) / float(var_2)
    return int(res + 0.5)


def main():
    try:
        arguments = re.split(r'(\D)', sys.argv[1])
        answer = ordering_operations(arguments)
        print(answer)
    except Exception as err:
        print(ERROR_MSG.format(err))


if __name__ == '__main__':
    main()
