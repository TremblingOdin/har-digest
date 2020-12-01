#!/usr/bin/python3

import argparse,json,sys

def diff(flist, outfile, avoid):
    print('Creating the diff file in: ', outfile)
    if len(flist) < 2:
        print("Pass at least 2 files to be compared")
    
    writer = open(outfile, 'w')
    try:
        nJson = None
        for f in flist:
            print("Reading file: ", f)
            reader = open(f, 'r')
            data = json.load(reader)
            if nJson is None:
                nJson = data
            else:
                print("new nJson count: ", nJson)
                for ent in data['log']['entries']:

                    found = False
                    removable = None
                    for entry in nJson['log']['entries']:
                        if ent['request'] == entry['request']:
                            found = True
                            removable = entry

                    if found:
                        nJson['log']['entries'].remove(removable)
                    else:
                        nJson['log']['entries'].append(ent)

            reader.close()
        
        for entry in nJson['log']['entries']:
            ending = entry['request']['url'].split(".")
            if ending in avoid:
                nJson['log']['entries'].remove(removable)
        json.dump(nJson, writer)
    finally:
        writer.close()

def union(flist, outfile):
    print('Creating the union file in: ', outfile)
    writer = open(outfile, 'w')
    try:
        reader = open(flist[0], 'r')
    finally:
        reader.close()
        writer.close()


def main(argv):
    parser = argparse.ArgumentParser(description='Help process HAR files')
    parser.add_argument('-a', '--avoid', help='file endings you want to ignore requests to')
    parser.add_argument('-o', '--output', help='the file to write to', action='store', required=True)
    parser.add_argument('-d', '--diff', help='find the difference between the input files', action='store_true')
    parser.add_argument('-u', '--union', help='merge the files together', action='store_true')
    parser.add_argument('vars', nargs='*', help='files to read from')
    args = parser.parse_args(argv)

    if args.avoid is not None:
        avoid = args.avoid.split()

    if args.diff and args.union:
        print("please only choose -d/--diff OR -u/--union not both")
    elif args.diff:
        diff(args.vars, args.output, avoid)
    elif args.union:
        union(args.vars, args.output)

if __name__ == '__main__':
    main(sys.argv[1:])
