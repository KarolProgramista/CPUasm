import argparse
import sys

def load_code():
	ap = argparse.ArgumentParser()

	ap.add_argument("infile", help="Input file name")
	ap.add_argument("-o", "--output", required=False, help="Output file name")
	args = vars(ap.parse_args())

	infile = args['infile']
	outfile = args['output'] if args['output'] else "a.bin"

	fp = open(infile, "r")
	code =  fp.read()
	fp.close()

	return [code, outfile]


