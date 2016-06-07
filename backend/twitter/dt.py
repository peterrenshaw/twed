#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


#===
# name  twed.backend.twitter.dt.py
# date: 2016JUN07
#       2013AUG30
# prog: pr
# desc: datetime tools work for twed (bigbox)
# lisc: moving towards GPL3
#
# copy: copyright (C) 2013-2016 Peter Renshaw
#===


import os
import time
import os.path
import datetime



#--- datetime tools ---
#
#---
# db_datetime_utc: return epoch in utc
#---
def db_datetime_utc():
    """store datetime in UTC epoch format"""
    t = datetime.datetime.utcnow()
    return time.mktime(t.timetuple())
def dt_datetime_strf(strf_fmt="%Y%b%d"):
    return datetime.datetime.now().strftime(strf_fmt).upper()
def fn_current_day(ext="json"):
    return "%s.%s" % (dt_datetime_strf(), ext)
#--- end datetime tools---


# main: cli entry point
def main():
    """main cli entry point"""
    print("dt.py usage:")
    utc = db_datetime_utc()
    print("\tdb_datetime_utc={}".format(utc))
    strf = dt_datetime_strf()
    print("\tdb_datetime_strf={}".format(strf))
    cd = fn_current_day()
    print("\tfn_current_day={}".format(cd)) 


if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
