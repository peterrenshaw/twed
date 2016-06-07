#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


import sys


# main cli enty point
def main():
    try:
        import twython
        from twython import Twython
    except:
        print('error: twython will not load')
        print('warning: try python3 ./status.py')
        sys.exit(1)
    tw_len = len(dir(Twython))
    if tw_len > 0:
        print('twython has %s modules' % tw_len)


# main cli entry point
if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
