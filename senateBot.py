# senateBot.py

import praw
import re

# Reddit API login, creds via praw.ini
reddit = praw.Reddit('senateBot', user_agent='senate_bot by Lukas Horak v0.2')

# active Subs - switch out which one is commented-out for easy testing purposes
subreddit = reddit.subreddit('testingground4bots')
#subreddit = reddit.subreddit('prequelmemes')

# Phrase which triggers senateBot
keyword = 'senate'

'''
TODO - Check replies to comments? (for "not yet")
'''

# Find phrase and inform them of who the Senate is
for comment in subreddit.stream.comments():
    if keyword in comment.body:
        try:
            reply = ''
            hits = re.findall(r"[^.]*?senate[^.]*\.", comment.body, flags=re.I)
            for phrase in hits:
                phr = re.compile(re.escape('senate'), re.IGNORECASE)
                reply += "> " + phr.sub('***SENATE***', phrase) + "\n\n"
            reply += "\n\n[I ***AM*** THE SENATE](https://www.youtube.com/watch?v=_MHusGl9BeM)\n\n"
            reply += "---\n\nThis is a bot designed to make sure the treasonous Jedi realise Chancellor Palpatine IS the senate"
            #comment.reply(reply)
            print(reply)

            print("posted")
        except Exception as e:
            print("senateBot fucked up...\n\n", e)

# URL for "Not Yet" - (https://www.youtube.com/watch?v=03HOhd4GI1w#t=27s)
