import sys
import argparse

from src.Parser import parseIn, parseOut

def main(argv=None):

    parser = argparse.ArgumentParser(description='Solve problem')

    parser.add_argument('--input',   help='Path to input file.', required=True)
    parser.add_argument('--output',  help='Path to output file', required=True)

    args = parser.parse_args(argv)

    inPath  = args.input
    outPath = args.output

    print("Parsing...")
    # TODO

    print("Solving...")
    # TODO

    # write solution to file
    print("Writing solution to file...")
    # TODO

    print("Done")


if __name__ == '__main__' :
    sys.exit(main())
