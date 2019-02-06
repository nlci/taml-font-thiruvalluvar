#!/bin/python3

from addcharslib import *

def modifySource(sfd, f, s, sn):
    print(sfd)

    workshop = 1.4
    roman = 0.9
    if f == 'ThiruValluvar':
        upm = 1.0
        devaf = 'Panini'
    else:
        upm = 1000.0/2048.0
        devaf = 'Maurya'
    scale = '-s ' + str(roman*upm) + ' '
    scaleSrc = '-s ' + str(upm/workshop) + ' '

    if f != 'Auvaiyar':
        cmd = scaleSrc + '-i ' + findFile('ThiruValluvar' + s + '.sfd') + ' --name u0B95_u0BC2'
        modifyFile(cmd, sfd)

    cmd = scaleSrc + '-i ' + findFile('ThiruValluvar' + '-R.sfd') + ' --rangefile grantha.usv --namefile grantha.name'
    modifyFile(cmd, sfd)

    asn = sn
    asn = asn.replace('BoldItalic', 'Bold')
    asn = asn.replace('Italic', 'Regular')
    cmd = scale + '-i ' + annapurna + asn + '.ttf' + ' --rangefile cs/annapurna/main.txt'
    modifyFile(cmd, sfd)

    if f == 'Auvaiyar':
        cmd = scale + '-i ' + charis + s + '.ttf' + ' -n uni0334.Lrg -n uni03A9 --rangefile cs/charis/pre.txt --rangefile cs/charis/main.txt'
        modifyFile(cmd, sfd)
    else:
        gs = s.replace('-', '')
        cmd = scale + '-i ' + gentium + gs + '.ttf' + ' --namefile cs/gentium/main_glyphs.txt --rangefile cs/gentium/pre.txt --rangefile cs/gentium/main.txt'
        modifyFile(cmd, sfd)
        cmd = scale + '-i ' + charis + s + '.ttf' + ' --rangefile cs/charis/composite4gentium.txt --rangefile cs/charis/extra4gentium.txt'
        modifyFile(cmd, sfd)

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        sn = sn.replace(' ', '')
        modifySource(f + '-' + sn + '.sfd', f, s, sn)
