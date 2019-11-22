import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help = "some help?")
parser.add_argument("-v", "--verbose", action = "store_true", help = "some help too?")
arg = parser.parse_args()
my_arg = arg.square
print(my_arg, " Parsed arguments")
