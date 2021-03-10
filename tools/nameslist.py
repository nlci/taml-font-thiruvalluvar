#!/usr/bin/python3

Vowels = [
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

Matras = [
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
    ]

MatrasPlus = [
    0x030C,  # COMBINING CARON
    0x034C,  # COMBINING ALMOST EQUAL TO ABOVE
    0x032D,  # COMBINING CIRCUMFLEX ACCENT BELOW
    ]

Consonants = [
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

Nuktas = [
    0x1133B,  # COMBINING BINDU BELOW
    0x1133C,  # GRANTHA SIGN NUKTA
    ]

Virama = [
    0x0BCD,  # TAMIL SIGN VIRAMA
    ]

Digits = [
    0x0BE6,  # TAMIL DIGIT ZERO
    0x0BE7,  # TAMIL DIGIT ONE
    0x0BE8,  # TAMIL DIGIT TWO
    0x0BE9,  # TAMIL DIGIT THREE
    0x0BEA,  # TAMIL DIGIT FOUR
    0x0BEB,  # TAMIL DIGIT FIVE
    0x0BEC,  # TAMIL DIGIT SIX
    0x0BED,  # TAMIL DIGIT SEVEN
    0x0BEE,  # TAMIL DIGIT EIGHT
    0x0BEF,  # TAMIL DIGIT NINE
    ]

vowels = list(map(chr, Vowels))
matras = list(map(chr, Matras))
matras_plus = list(map(chr, MatrasPlus))
consonants = list(map(chr, Consonants))
nuktas = list(map(chr, Nuktas))
h = virama = list(map(chr, Virama))[0]
digits = list(map(chr, Digits))

ka = consonants[0]
ssa = consonants[20]

Akhands = [
    ka + virama + ssa,  # KaSsa
    ]

akhands = Akhands
