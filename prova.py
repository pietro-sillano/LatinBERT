import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', help='path of output txt', required=False)
args = vars(parser.parse_args())
print(args["output"])
