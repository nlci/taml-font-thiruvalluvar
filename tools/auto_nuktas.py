#!/usr/bin/python3

from nameslist import *
import sys


with open(sys.argv[1], 'w') as output:
    output.write('RenderingUnknown\n')

    for c in consonants + akhands:
        for m in [''] + matras + [h]:
            clusters = list()
            cluster = c + m
            clusters.append(cluster)
            for n in nuktas:
                cluster = c + m + n
                clusters.append(cluster)
                cluster = c + n + m
                clusters.append(cluster)
                cluster = c + n + m + n
                clusters.append(cluster)
            line = ' '.join(clusters) + '\n'
            output.write(line)

    for v in vowels:
        clusters = list()
        for n in [''] + nuktas:
            cluster = v + n
            clusters.append(cluster)
        line = ' '.join(clusters) + '\n'
        output.write(line)
