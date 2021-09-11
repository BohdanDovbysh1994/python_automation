from argparse import ArgumentParser

# example 1
parser = ArgumentParser()
parser.add_argument('--a', help='first argument of sum operation', default=5)
parser.add_argument('--b', help='second argument of sum operation', default=5)

args = parser.parse_args()
arguments = {key: float(value) for key, value in args.__dict__.items()}
print(f"{arguments['a']} + {arguments['b']} = {arguments['a'] + arguments['b']}")

# example 2
# parser = ArgumentParser(description='Process some integers.')
# parser.add_argument(
#     'integers', metavar='N', type=int, nargs='+',
#     help='an integer for the accumulator'
# )
# parser.add_argument(
#     '--sum', dest='accumulate', action='store_const', const=sum, default=max,
#     help='sum the integers (default: find the max)'
# )
#
# args = parser.parse_args()
# print(type(args.integers))
# print(args.accumulate(args.integers))