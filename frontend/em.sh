#!/bin/sh


#======
# name: em.sh
# date: 2016MAY22
# prog: pr
# desc: elm make script WIN specific calls
#
#       build script for elm make
#       specificly a shell script as 
#       it execute on a windows box 
#       sans make
#
# sec : on linux read this 
#       <https://sipb.mit.edu/doc/safe-shell/>
#======


{
    clear

    echo "elm make"
    elm-make --output target/ed.js src/form.elm
    cp target/ed.js ../js
    ls ../js

}>&2
