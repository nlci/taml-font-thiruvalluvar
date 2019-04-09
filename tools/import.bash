#!/bin/bash

face="$1"
style="$2"
ufo="$3"

if [ "${face}" = "ThiruValluvar" ]
then
    devaf="Panini"
else
    devaf="Maurya"
fi

psfcopyglyphs -f --rename rename --unicode usv -i ../cs/panini/main4taml.csv -s "${deva}/${devaf}-${style}.ufo" ${ufo}
