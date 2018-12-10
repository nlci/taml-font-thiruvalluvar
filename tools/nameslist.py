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

vowels = list(map(chr, Vowels))
matras = list(map(chr, Matras))
consonants = list(map(chr, Consonants))
nuktas = list(map(chr, Nuktas))
h = virama = list(map(chr, Virama))[0]

ka = consonants[0]
ssa = consonants[20]

Akhands = [
    ka + h + ssa,  # KaSsa
    ]

akhands = Akhands
