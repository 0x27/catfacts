#!/usr/bin/python2
# coding: utf-8
# catfacts - a lovely SMS sending tool
# ~0x27
# TODO: Write a reply handling thread with automatically generated
# bollocks.
import random
from time import sleep
from twilio.rest import TwilioRestClient
import sys

# global variables. change these...
sender = "CATFACTS"
account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"

def send_sms(phone, message):
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=phone, from_=sender, body=message)
    print "{*} Message sent!"
    
def cat_facts(victim):
    print "{+} Launching catfacts against %s" %(victim)
    try:
        for line in open("catfacts.txt").readlines():
            print "{+} Sending Message!"
            try:
                send_sms(phone=victim, message=line)
            except Exception:
                print "{!} There was an error sending your message!"
                pass
            wait_time = random.randint(300, 3600)
            print "{+} Sleeping for %d" %(wait_time)
            time.sleep(wait_time)
        print "{+} Catfacts expended!"
    except KeyboardInterrupt:
        sys.exit("{-} Catfacts Terminated!")
        
def main(args):
    if len(args) != 2:
        sys.exit("use: %s <victimphone>" %(args[0]))
    cat_facts(victim=args[1])

if __name__ == "__main__":
    main(args=sys.argv)
