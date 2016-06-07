#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


#===
# name  twed/backend/twitter/system.py
# date: 2016JUN07
#       2013AUG30
# prog: pr
# desc: file and conversion tools for twed (bigbox)
# lisc: moving towards GPL3
#
# copy: copyright (C) 2013 - 2016 Peter Renshaw
#===


import os
import sys
import json
import platform # removed sys.platform in 3.3
import os.path


#------
# root from where installed code
# potential failure point of save      
#------
ROOT_LIN = "/code"
ROOT_WIN = "d:\\"



# TODO more testing #$@%^@^!
# 2016JUN07
# - testing of paths for installed code
# - testing of paths for incorrect path
# 2016JAN19
# - hard coded the 'code' file path so if you changed the 
#   root file path, fails.
# - forgot to import sys
# 2014JAN06
# - should handle for now, my movement of 
#   code save points. This has to be looked at
#   better. Maybe defining a save point in defaults
#   that you know exactly the path & what OS we are on
#----


#----
# WARNING: THIS CODE WILL POTENTIALLY FAIL
#          WITHOUT CORRECT PATHS PRESENT
#----
PLATFORM = platform.system()
if PLATFORM == 'Linux':
    MOUNT_POINT = ROOT_LIN
elif PLATFORM == 'Windows':
    MOUNT_POINT = ROOT_WIN
else:
    print("Error: no recognizable platform")
    print("\tplatform: <%s>" % platform.system())
    sys.exit(1)
#----
# WARNING: THIS CODE WILL POTENTIALLY FAIL
#          WITHOUT CORRECT PATHS PRESENT
#----


# path used for saving files in 
# twed/backend/tweets (bigbox/feed/tweets)
#REL_PATH = os.path.join(MOUNT_POINT,'code', 'bigbox', 'bigbox')
REL_PATH = os.path.join(MOUNT_POINT, 'twed', 'backend', 'tweets')
if not os.path.isdir(REL_PATH):
    print("Error: invalid directory path in tools.system")
    print("\tplatform: <%s>" % platform.system())
    sys.exit(1)


#--- filesystem tools ---
def save(filepathname, data):
    """save a file to filesystem"""
    filepath = os.path.dirname(filepathname)
    filename = os.path.basename(filepathname)
    if data:
        if filename:
            if os.path.isdir(filepath):
                with open(filepathname, 'w') as f:
                    f.write(data)
                return True
    return False
def load(filepathname):
    """load a file"""
    if filepathname: 
        if os.path.isfile(filepathname):
            data = ""
            with open(filepathname, 'r') as f:
                data = f.read()
            f.close()
            return data
    return False

# TODO confusing - returns filepath built from
#                  relative path + directory + filename
# path_absolute: return valid filepath or F
def path_absolute(filepath_directory, filename, 
                  filepath_relative=REL_PATH):
    """return valid abolute filepath or F"""
    if filepath_relative and filepath_directory and filename:
        fpr = os.path.join(filepath_relative, filepath_directory, 
                           filename)
        if os.path.isfile(fpr):
            return fpr
    return False
#--- end filesystem tools ---


#---
# convert: bi-directional conversion of data from
#          py=>json or json=>py. indent_sz arg 
#          for display, reduce to zero to save
#          space.
#---
def convert(data, to_json=True, indent_sz=4):
    """conversion from py<==>json"""
    if data:
        if to_json:
            return json.dumps(data, sort_keys=True, indent=indent_sz, 
                              separators=(',', ': '))
        else:
            return json.loads(data)
    return False
def json2py(data):
    """convert json data to python structure"""
    return convert(data, to_json=False)
#---
# py2json: convert python data structure to json
#          indent arg reduces data size
#---
def py2json(data, indent=4):
    """convert python structure to json"""
    return convert(data, to_json=True, indent_sz=indent)
#--- end conversion tools ---


# TODO testing please 2013OCT02
#--- boolean string conversion ---
#
def str2bool_false(v=""):
    v = str(v)  # TODO check if this is a good idea - probably not
    return v.lower() in ("", "no", "false", "f", "0")
def str2bool_true(v=""):
    v = str(v)
    return v.lower() in ("yes", "true", "t", "1")
#---
# str2bool: test if str value is T/F
#---
def str2bool(v, is_test_true=True):
    """is input str input boolean T/F, toggle is_test_true"""
    v = str(v)
    if is_test_true:
        # if str tests explicit T, return True
        return True if str2bool_true(v) else False
    else:
        # if str tests explicit F, return False
        return False if str2bool_false(v) else True
#--- end boolean string conversion ---


# main: cli entry point
def main():
    """main cli entry point"""
    pass

if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
