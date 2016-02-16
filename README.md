Dota2Twitter
============

Want to spam your followers with irrelevant, pointless video game 
matches you played with nine random internet strangers? Here you go. This is 
the best way to listen for new Dota matches and post them to Twitter!

# Install

Copy the repo locally somewhere on a device that will be on probably 24/7 
and won't mind having a terminal open in, or a server that you can remote 
into and run this in the background (either forking to background or 
multiplexing it via screen/tmux)

```
$ git clone https://github.com/sleibrock/Dota2Twitter
```

After that we need to install packages from Pip, so if you don't have Pip, 
do this

```
$ easy_install -U pip
```

Then finally we can do

```
sudo make setup
```

This will install packages listed in the requirements text and also create a 
local configuration file that you will need to edit with your Twitter 
information, as well as your public Dota 2 Steam ID.

After that, to run the daemon
```
make
```

Then sit back and watch all your favorites/retweets pile up, bro.

# How do I allow this to access my Twitter?

You need to register an "app" to your Twitter account, get consumer/access 
tokens and secrets, then put those keys into the configuration file. Then, 
we can start sending requests to the Twitter API.

# What's my Dota 2 ID?

You need to enable public match sharing so your name will come up in the 
Dota 2 JSON API. After that you can find your ID somewhere in the game's client, 
or you can log in through Steam on Dotabuff and find your profile directly.

# Why does this stupid thing take so long to update?

Hold on there buddy, these services are free, but that doesn't mean we 
have to spam thousands of requests within a couple of seconds. That's an 
easy way to get IP banned.

The average game of Dota lasts about forty minutes. The daemon will 
look once every hour for a Player's profile, scan if there's a new match 
(based on previous match checks), and then post it to Twitter. This program 
will NOT post every game in your history, nor will it ever because no one 
cares about games from two years ago. It only cares about what's new, 
while the daemon is running.

# Credits

Here's the sites used:

* [Dotabuff](http://www.dotabuff.com/)
* [Twitter](https://twitter.com/)
