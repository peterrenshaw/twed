#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


#=====
# name: rserve.py
# date: 2016MAY01: added CORS support
#       2016APR28: checkin
# prog: pr
# desc: toy twitter poster
# updt: added CORS support using Flask Cors
#       <https://github.com/corydolphin/flask-cors>
# src : <https://docs.python.org/2/library/random.html#random.SystemRandom>
#=====


import os
import sys
import random
from optparse import OptionParser


from flask import Flask
from flask.ext.cors import CORS


PORT = 8090


app = Flask(__name__)
CORS(app)
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='febonehead'
))

@app.route('/')
def index():
    return "{}".format(random.randint(0, 128))


if __name__ == "__main__":
    app.run('0.0.0.0', port=PORT)


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
