#!/bin/python

import os
import os.path
import sys
from wscript import *

cs = '../../../../work/nlci/projects/fonts/charsets/'
charis = '../../../latn/fonts/charis_local/5.000/zip/unhinted/CharisSIL'
gentium = '../../../latn/fonts/gentium_local/basic/1.102/zip/unhinted/GenBkBas'
annapurna = '../../../deva/fonts/annapurna_local/1.203/zip/unhinted/AnnapurnaSIL-'
badami = '../badami/source'

def runCommand(cmd, filenames):
    cmd = 'ffcopyglyphs' + ' -f ' + cmd + ' ' + filenames
    print cmd
    os.system(cmd)

def findFile(filename):
    return os.path.join(sys.argv[1], filename)

def modifyFile(cmd, filename):
    tmp = 'tmp.sfd'
    os.rename(findFile(filename), tmp)
    runCommand(cmd, tmp + ' ' + findFile(filename))
    os.remove(tmp)

def modifySource(sfd, f, s, sn):
    print sfd

    if f != 'Auvaiyar':
        cmd = '-i ' + findFile(os.path.join('..', '..', 'source', 'ThiruValluvar' + s + '.sfd')) + ' --name u0B95_u0BC2'
        modifyFile(cmd, sfd)

    cmd = '-i ' + findFile(os.path.join('..', '..', 'source', 'ThiruValluvar-R.sfd')) + ' --rangefile grantha.usv --namefile grantha.name'
    modifyFile(cmd, sfd)

    cmd = '-i ' + charis + s + '.ttf' + ' -n uni0334.Lrg -n uni03A9 --rangefile cs/charis/pre.txt --rangefile cs/charis/main.txt'
    modifyFile(cmd, sfd)

    asn = sn
    asn = asn.replace('Bold Italic', 'Bold')
    asn = asn.replace('Italic', 'Regular')
    cmd = '-i ' + annapurna + asn + '.ttf' + ' --rangefile ' + os.path.join(cs, 'annapurna', 'indic.txt')
    # modifyFile(cmd, sfd)

    # ms = s.replace('-', '')
    # cmd = '-s 0.5 -i ' + gentium + ms + '.ttf' + ' --rangefile pre.txt --rangefile nrsi.txt --rangefile nlci.txt'
    # modifyFile(cmd, sfd)
    # findFile(os.path.join('..', 'results', f + '-' + sn.replace(' ', '') + '.ttf'))

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        sn = sn.replace(' ', '')
        modifySource(f + '-' + sn + '.sfd', f, s, sn)
