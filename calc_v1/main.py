import argparse

parser = argparse.ArgumentParser(description='Process some floats.')
parser.add_argument('integers', metavar='N', type=float, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('+', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
