#!/usr/bin/python3

from nameslist import *
import sys


with open(sys.argv[1], 'w') as output:
    output.write('RenderingUnknown\n')

    for mp in matras_plus:
        for c in consonants:
            clusters = list()
            for n in [''] + nuktas:
                for m in [''] + matras:
                    clusters.append(c + m + n + mp)
                    clusters.append(c + n + m + mp)
            line = ' '.join(clusters) + '\n'
            output.write(line)
