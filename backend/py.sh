#!/bin/sh

#======
# name: py.sh
# date: 2016MAY22
# prog: pr
# desc: quick hack for first time install 
#       of Pip, Flask and Flask-Cors      
# 
# usge: $ sudo ./py.sh
#      
# sec : on linux read this 
#       <https://sipb.mit.edu/doc/safe-shell/>
#======


{
    clear

    echo "install new pip"
    python -m pip install --upgrade pip

    echo "install Flask and Flask-Cors"
    pip3 install Flask
    pip3 install Flask-Cors

}>&2
