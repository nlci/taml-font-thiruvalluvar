#!/usr/bin/python3

def main():
    Generate.generate('../tests/generated.txt')

class Generate(object):

    def __init__(self):
        pass

    @staticmethod
    def generate(filename):
        """Output generated test data"""

        vowels = [
            0x0B85,  # TAMIL LETTER A
            0x0B86,  # TAMIL LETTER AA
            0x0B87,  # TAMIL LETTER I
            0x0B88,  # TAMIL LETTER II
            0x0B89,  # TAMIL LETTER U
            0x0B8A,  # TAMIL LETTER UU
            0x0B8E,  # TAMIL LETTER E
            0x0B8F,  # TAMIL LETTER EE
            0x0B90,  # TAMIL LETTER AI
            0x0B92,  # TAMIL LETTER O
            0x0B93,  # TAMIL LETTER OO
            0x0B94,  # TAMIL LETTER AU
            ]
        consonants = [
            0x0B95,  # TAMIL LETTER KA
            0x0B99,  # TAMIL LETTER NGA
            0x0B9A,  # TAMIL LETTER CA
            0x0B9C,  # TAMIL LETTER JA
            0x0B9E,  # TAMIL LETTER NYA
            0x0B9F,  # TAMIL LETTER TTA
            0x0BA3,  # TAMIL LETTER NNA
            0x0BA4,  # TAMIL LETTER TA
            0x0BA8,  # TAMIL LETTER NA
            0x0BA9,  # TAMIL LETTER NNNA
            0x0BAA,  # TAMIL LETTER PA
            0x0BAE,  # TAMIL LETTER MA
            0x0BAF,  # TAMIL LETTER YA
            0x0BB0,  # TAMIL LETTER RA
            0x0BB1,  # TAMIL LETTER RRA
            0x0BB2,  # TAMIL LETTER LA
            0x0BB3,  # TAMIL LETTER LLA
            0x0BB4,  # TAMIL LETTER LLLA
            0x0BB5,  # TAMIL LETTER VA
            0x0BB6,  # TAMIL LETTER SHA
            0x0BB7,  # TAMIL LETTER SSA
            0x0BB8,  # TAMIL LETTER SA
            0x0BB9,  # TAMIL LETTER HA
            ]
        matras = [
            0x0BBE,  # TAMIL VOWEL SIGN AA
            0x0BBF,  # TAMIL VOWEL SIGN I
            0x0BC0,  # TAMIL VOWEL SIGN II
            0x0BC1,  # TAMIL VOWEL SIGN U
            0x0BC2,  # TAMIL VOWEL SIGN UU
            0x0BC6,  # TAMIL VOWEL SIGN E
            0x0BC7,  # TAMIL VOWEL SIGN EE
            0x0BC8,  # TAMIL VOWEL SIGN AI
            0x0BCA,  # TAMIL VOWEL SIGN O
            0x0BCB,  # TAMIL VOWEL SIGN OO
            0x0BCC,  # TAMIL VOWEL SIGN AU
            0x0BCD,  # TAMIL SIGN VIRAMA
            ]
        nuktas = [
            0x1133B,  # COMBINING BINDU BELOW
            0x1133C,  # GRANTHA SIGN NUKTA
            ]
        with open(filename, 'w') as output:
            output.write('RenderingUnknown\n')

            vowel_chars = list(map(chr, vowels))
            consonant_chars = list(map(chr, consonants))
            matra_chars = list(map(chr, matras))
            nukta_chars = list(map(chr, nuktas))

            ka_virama_ssa = chr(0x0B95) + chr(0x0BCD) + chr(0x0BB7)
            consonant_chars.append(ka_virama_ssa)
            matra_chars.insert(0, '')

            for c in consonant_chars:
                for m in matra_chars:
                    clusters = list()
                    for n in nukta_chars:
                        cluster = c + m
                        clusters.append(cluster)
                        cluster = c + m + n
                        clusters.append(cluster)
                        cluster = c + n + m
                        clusters.append(cluster)
                        cluster = c + n + m + n
                        clusters.append(cluster)
                    line = ' '.join(clusters) + '\n'
                    output.write(line)

            nukta_chars.insert(0, '')
            for v in vowel_chars:
                clusters = list()
                for n in nukta_chars:
                    cluster = v + n
                    clusters.append(cluster)
                line = ' '.join(clusters) + '\n'
                output.write(line)

if __name__ == "__main__":
    main()
