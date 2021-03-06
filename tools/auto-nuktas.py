#!/usr/bin/python3

from nameslist import *
import sys


def add_virama(clusters, cluster):
    for h in [''] + [virama]:
        clusters.append(cluster + h)


with open(sys.argv[1], 'w') as output:
    output.write('RenderingUnknown\n')

    for c in consonants + akhands:
    # for c in consonants:
        for m in [''] + matras:
        # for m in [chr(0x0BC1), chr(0x0BC2)]:
            clusters = list()
            cluster = c + m
            add_virama(clusters, cluster)
            for n in nuktas:
                cluster = c + m + n
                add_virama(clusters, cluster)
                cluster = c + n + m
                add_virama(clusters, cluster)
                cluster = c + n + m + n
                add_virama(clusters, cluster)
            comment = ''
            # if m == chr(0x0BC1):
            #     comment = hex(ord(c)) + ' u'
            # elif m == chr(0x0BC2):
            #     comment = hex(ord(c)) + ' U'
            line = ' '.join(clusters) + comment + '\n'
            output.write(line)

    for v in vowels:
        clusters = list()
        for n in [''] + nuktas:
            cluster = v + n
            clusters.append(cluster)
        line = ' '.join(clusters) + '\n'
        output.write(line)
