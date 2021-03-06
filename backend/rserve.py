#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


#=====
# name: rserve.py
# date: 2016MAY22: reshape code as twit server
#       2016MAY01: added CORS support
#       2016APR28: checkin
# prog: pr
# desc: toy twitter poster
# src : added CORS support using Flask Cors
#       <https://github.com/corydolphin/flask-cors>
#=====


import os
import sys
import random
from optparse import OptionParser


from flask import Flask
from flask import render_template
from flask.ext.cors import CORS


PORT = 8090


app = Flask(__name__)
CORS(app)
app.config.update(dict(
    DEBUG=False,
    SECRET_KEY='febonehead'
))


#------
# index: editor page
#------
@app.route('/')
def index():
    """serve index page"""
    return render_template('index.html')



#------
# entry point
#------
if __name__ == "__main__":
    app.run('0.0.0.0', port=PORT)


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
