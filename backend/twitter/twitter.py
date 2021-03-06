#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


#===
# name: twitter.py
# date: 2016JUN07
#       2013SEP22
# prog: pr
# desc: code allows twitter integration with bigbox
#       Twython code allows full access to twit api
#       ...along with restrictions.
#
# lisc: moving towards GPL3
# copy: copyright (C) 2013-2016 Peter Renshaw
#
# use : 
#       send: twitter.py -m "'I hit the city and I lost my band'"
#       qry : twitter.py -q '#neilyoung'
#       help: twitter.py -h
#       vers: twitter.py -v
#
# sorc: <https://github.com/ryanmcgrath/twython>
#===


import sys
import os.path
from optparse import OptionParser


from twython import Twython
from twython import TwythonError


import dt
import config
import system
from system import REL_PATH


# TODO 
#     * build 1/2 decent way to extract all data
#       from twitter query, not hard
#     - needs regular testing to see if api changes
#     * check twitter restrictions
#       on search
#     * implement a twitter search count/min
#     * create extraction object for better extraction
#     * internet connected
#     * not get secrets data into github
#     * testing
#     * work out how to:
#     - report errors, halt/return code?
#     - save to filesystem/api?
#



#---
# authenticate_rw: pass in keys, object & return authenticated
#                  for full API access to twitter Twython object or F
#---
def authenticate_rw(consumer_key, consumer_secret, 
                    access_key, access_secret):
    """
    authenticate Twython object with keys & secrets, return obj or F
    """
    status = False
    try:
        status = Twython(consumer_key, consumer_secret, 
                         access_key, access_secret)
    except TwythonError as e:
        status = False
    return status



#---
# name: Twy_rw
# date: 2016JUN07
#       2013SEP22
# prog: pr
# desc: simple wrapper for Twython object
#       RW access to twitter API
#       have to pass in valid Twython obj
#       so remember to initialise
#---
class Twy_rw:
    def __init__(self, twitter_obj):
        """init Twy object"""
        self.max_msg_length = 140
        self.twitter = twitter_obj
        self.message = ""
        self.message_id = 0
        #
        # TODO check Twython obj valid
        #
    def valid(self):
        """is object valid?"""
        # TODO this really doesn't do the job
        #      seems to return obj even without
        #      consumer & access keys
        if self.twitter: return True
        else: return False
    def message_len(self):
        """return length of message"""
        # expect F, use zero
        return len(self.message) if self.message else 0  
    def valid_message_length(self):
        """check message length is correct"""
        if self.message_len() > 0:
            if self.message_len() <= self.max_msg_length:
                return True
        return False
    #---
    # build_data: extract data from twitter api call, decode & build
    #             dictionary to save. Failed? try url below:
    # <https://dev.twitter.com/docs/api/1.1/get/statuses/show/%3Aid>
    #
    # original data structure:
    #    line = """{"message": "%s","status": "%s","date": %s}\n""" % 
    #              (message, update.id, time.mktime(t.timetuple())) 
    #
    #---
    def build_data(self, tid, tmsg, tent):
        """build dict of data to save to file"""
        if tid:  # have twitter id?
            if tmsg: # have a twitter message?
                if tent: # have a twitter entitiy? (complicated)

                    # gracefully fail if we screw up
                    try:
                        dtags = tent['hashtags']
                        durls = tent['urls']

                        # will this survive json if not str?
                        dt_str = "%s" % dt.db_datetime_utc()

                        #---
                        # data structure for storage
                        py_data = dict(id_str=tid,              # tweet id
                                       message=tmsg,            # msg sent
                                       hashtag=tent['hashtags'],# list of #tags 
                                       urls=tent['urls'],       # list of urls
                                       date_str=dt_str)         # epoch in utc
                        #---
                    except:
                        return False
                    return py_data
        return False
    def save(self, tid, tmsg, tent, fp_rel=REL_PATH):
        """save message to somewhere"""
        # TODO
        # work out if saved previously and give better response
      

        # save to file system/rest api? where?
        # save to filesystem
        # TODO what day is this? localtime?
        fn = dt.fn_current_day(ext='json')

        # TODO fix: warning on hard coded file paths
        fp = os.path.join(fp_rel)  
        #print("fn={}\nfp={}".format(fn, fp))

        # print("twitter.save() fp=<%s>" % fp)
        if os.path.isdir(fp):
            fpn = os.path.join(fp, fn)
            with open(fpn, 'a') as f:
                # TODO: kill if fails
                #print("tid={}\ntmsg={}\ttent={}".format(tid, tmsg, tent))
                line_py = self.build_data(tid, tmsg, tent)
                line_json = system.py2json(line_py)

                #print("line_py={}".format(line_py))
                #print("line_json={}".format(line_json))

                f.write(line_json)
                f.write('\n')  # stops braces butting up
            return True       

        return False
    def send(self, message):
        """send a message"""
        self.message = message
        status = False
        # only send if valid length
        if self.valid_message_length():
            # catch Twython errors
            try:
                # twitter api call, (trim_user) only ret what we need
                s = self.twitter.update_status(status=self.message,
                                               trim_user=True)

                t_id = s['id_str']    # twitter id as string
                t_msg = s['text']     # twitter message
                t_ent = s['entities'] # twitter urls, tags & misc

                if self.save(t_id, t_msg, t_ent):
                    return t_id
                else:
                    return False
            except TwythonError as e:
                return False
        return status
    def close(self):
        """de-allocate Twython object"""
        self.twitter = None
        return True


#---
# main cli entry point
#---
def main():
    """main cli entry point"""
    usage = "usage: %prog [v] -t -d"
    parser = OptionParser(usage)

    # --- options ---
    parser.add_option("-m", "--message", dest="message", \
                      help="send a message")
    parser.add_option("-q", "--search", dest="search", \
                      help="search twitter by query")
    parser.add_option("-v", "--version", dest="version",
                      action="store_true",
                      help="current version")    
    options, args = parser.parse_args()

    # --- process ---
    if options.version:
        print("%s v%s %s %s" % ('twed', bigbox.__version__, 
                                '2016JUN07', '(C) 2013-2016'))
        sys.exit(0)
    elif options.message:
        twitter = authenticate_rw(config.CONSUMER_KEY,
                                  config.CONSUMER_SECRET,
                                  config.ACCESS_KEY,
                                  config.ACCESS_SECRET)
        if twitter:
            t = Twy_rw(twitter)
            print("send")
            status = t.send(options.message)
            print("status={}".format(status))
            if status:
                print("message saved & sent (%s)" % t.message_len())
                print("ack")
            else:
                print("cant send message (%s)" % t.message_len())
                print("fail")
        else:
            print("bad Twython object, check")

        t.close()
    elif options.search:
        print("query = <%s>" % options.search)
        twitter = authenticate_r(config.CONSUMER_KEY,
                                 config.CONSUMER_SECRET,"")
        if twitter:
            t = Twy_r(twitter)
            if t: 
                result = t.search(options.search, count=5)
                t.save(result)
                print("ack")      
            else:
                print("fail")
        else:
            print("bad Twython object, check")
    else:
        parser.print_help()
    # --- end process ---


# main cli entry point
if __name__ == "__main__":
    main()


# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab
