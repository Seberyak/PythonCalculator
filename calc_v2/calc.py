import sys

ERROR_MSG = "(Error: {})"


def split(args):
    res, var = [], ""
    for i in args:
        if i in "+-*/":
            res += [int(var), i]
            var = ""
            continue
        var += i
    return res + [int(var)]


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
    return int(args[0]+0.5)


def calculate(var_1, operand, var_2):
    res = 0
    if operand == "+":
        res = float(var_1 + var_2)
    if operand == "-":
        res = float(var_1 - var_2)
    if operand == "*":
        res = float(var_1 * var_2)
    if operand == "/":
        res = float(var_1 / var_2)
    return res


def main():
    try:
        arguments = split(sys.argv[1])
        answer = ordering_operations(arguments)
        print(answer)
    except Exception as err:
        print(ERROR_MSG.format(err))


if __name__ == '__main__':
    main()
