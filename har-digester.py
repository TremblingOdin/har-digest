#!/usr/bin/python3

import argparse,sys

def diff(flist, outfile):
    print('Creating the diff file in: %s', outfile)
    writer = open(outfile, 'w')
    try:
        reader = open(flist[0],'r')
    finally:
        reader.close()
        writer.close()

def union(flist, outfile):
    print('Creating the union file in: % s', outfile)
    writer = open(outfile, 'w')
    try:
        reader = open(flist[0], 'r')
    finally:
        reader.close()
        writer.close()


def main(argv):
    parser = argparse.ArgumentParser(description='Help process HAR files')
    parser.add_argument('-o', '--output', help='the file to write to', action='store', required=True)
    parser.add_argument('-d', '--diff', help='find the difference between the input files', action='store_true')
    parser.add_argument('-u', '--union', help='merge the files together', action='store_true')
    parser.add_argument('vars', nargs='*', help='files to read from')
    args = parser.parse_args(argv)

    if args.diff and args.union:
        print("please only choose -d/--diff OR -u/--union not both")
    elif args.diff:
        diff(args.vars, args.output)
    elif args.union:
        union(args.vars, args.output)

if __name__ == '__main__':
    main(sys.argv[1:])
