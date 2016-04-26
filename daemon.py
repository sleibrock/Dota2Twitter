#!/usr/bin/env python
#-*- coding: utf-8 -*-

from sys import argv
from time import sleep, time 
from json import load as jload
from random import choice

from tweepy import API, OAuthHandler

from D2T.Match import *
from D2T.Player import *

sleepy_time = 3600 

# Messages for winning
win_msgs = [
    "Won with {}",
    "{} victory",
    "ez {} game",
]

# Messages for when you lose
fail_msgs = [
    "Whoops",
    "Game is hard",
    "I immediately regret my decision",
    "я потерял гг",
    " ¯\_(ツ)_/¯",
]

URL = "http://www.dotabuff.com/matches/{0}"

def stats(pstat):
    '''
    Quickly format a PStat into a string for tweets
    '''
    return "(kda:{0} gpm:{1})".format(pstat.kda, pstat.gpm)

def create_logger(enable_logging=False):
    '''
    Create a logging method based on logging being enabled or not
    '''
    if enable_logging:
        def log(msg):
            print("[{}] {}".format(int(time()), msg)) 
    return lambda x: None

def main(*args, **kwargs):
    '''
    Main daemon application
    1. Reads in a configuration file given
    2. Opens up access to a Twitter account
    3. Fetches a player's profile page
    4. Checks the last match updated in a local cache
    5. Finds the "newest" match to update to Twitter
    6. Pulls the match ID to update to Twitter
    7. Analyzes it and makes a snobbish post to Twitter
    '''
    # Read in a configuration file from sys.argv
    try:
        conf = jload(open(argv[1], 'r')) 
    except Exception as e:
        print(str(e))
        print("Invalid or no configuration supplied")
        print("Command: D2T-Daemon JSON_CONF_FILE")
        quit()

    # Create the Twitter Oauth instance
    try:
        auth = OAuthHandler(conf["consumer_key"], conf["consumer_secret"])
        auth.set_access_token(conf["access_key"], conf["access_secret"])
        api = API(auth)
    except Exception as e:
        print(str(e))
        print("Failed to create Twitter connection")
        quit()

    # create the logging instance
    log = create_logger("-d" in argv or "--debug" in argv)
       
    # Begin while loop to infinity
    my_pid = conf["player_id"]
    try:
        log("Beginning daemon...")
        while True:
            # Open up local cache to see what the last match was
            try:
                with open(".last_match", "r") as f:
                    contents = f.read()
                last_match = int(contents)
            except Exception:
                log("Cache not found, setting to 0...")
                last_match = 0

            log("Getting player {}...".format(conf["player_id"]))
            player = get_player(my_pid)

            # Flag for when we already did something
            already_done = False

            # If we have no match cache
            if last_match == 0 or last_match is None:
                new_match = player.matches[-1]
            else:
                if last_match == player.matches[0]:
                    log("No new matches")
                    already_done = True
                else:
                    found_match = False
                    checked_match = 0
                    for matchnum in player.matches:
                        if last_match == matchnum:
                            found_match = True
                        if not found_match:
                            checked_match = matchnum
                    new_match = checked_match

            if not already_done:
                log("Getting match {}...".format(new_match))
                match = get_match(new_match)

                radi_stats  = [p for p in match.radiant if p.id == my_pid]
                dire_stats  = [p for p in match.dire if p.id == my_pid]

                # Check for player's ID in both teams to infer their team
                if radi_stats:
                    my_team = "Radiant"
                    pstat   = radi_stats.pop()
                else:
                    my_team = "Dire"
                    pstat   = dire_stats.pop()

                # Finally...
                if my_team == match.victor:
                    msg = choice(win_msgs).format(pstat.hero)
                else:
                    msg = choice(fail_msgs).format(pstat.hero)

                tweet = " ".join([msg, stats(pstat), "-", URL.format(new_match)])
                log("Posting {}".format(tweet))
                
                api.update_status(tweet)

                # Write to local cache
                with open(".last_match", "w") as f:
                    f.write(str(new_match))

            log("Resting...")
            sleep(sleepy_time)
    except Exception as e:
        print("Something went completely wrong")
        print(e)
    except KeyboardInterrupt:
        print("\nLeaving")
    finally:
        log("Exiting Daemon")

if __name__ == "__main__":
    main()
# end
