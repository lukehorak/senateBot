# senateBot

import praw
#from PyDictionary import PyDictionary
#import enchant
import re

# reddit API login, creds via praw.ini
reddit = praw.Reddit('senateBot', user_agent='senate_bot by Lukas Horak v0.2')

# active Subs
subreddit = reddit.subreddit('testingground4bots')

# phrase to activate the bot
keyword = 'senate'

# Find phrase and inform them of who the Senate is
for comment in subreddit.stream.comments():
    if keyword in comment.body:
        try:
            reply = ''
            hits = re.findall(r"[^.]*?senate[^.]*\.", comment.body, flags=re.I)
            for phrase in hits:
                phr = re.compile(re.escape('senate'), re.IGNORECASE)
                ph = phr.sub('***SENATE***', phrase)
                reply += "> " +  ph + "\n\n[I ***AM*** THE SENATE](https://www.youtube.com/watch?v=_MHusGl9BeM)\n\n"
            comment.reply(reply)

            print("posted")
        except:
            print("fail")
