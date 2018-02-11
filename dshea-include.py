#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print(sys.argv[0] + ' <file1 [file2 ...]>')
    sys.exit(0)

for filename in sys.argv[1:]:
    print(filename)

    with open(filename) as f:
        content = f.readlines()

    fout = open(filename, 'w')
    insertFilename = 'stuff'
    outputFlag = True
    for line in content:

        if '<!-- dshea-include BEGIN' in line:
            fout.write(line)
            outputFlag = False
            insertFilename = line.split()[3]
            print('  inserting: ' +  insertFilename)
            with open(insertFilename) as insertFile:
                for line in insertFile:
                    fout.write(line)
        
        if '<!-- dshea-include END' in line:
            outputFlag = True

        if outputFlag:
            fout.write(line)

    if not outputFlag:
        print('  WARNING: include file ' + insertFilename + ' Never saw an END')
        
    fout.close()

