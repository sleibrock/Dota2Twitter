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
make run
```

After that the client runs on it's own. You can fork it as well, or use
a screen multiplexer such as GNU Screen or Tmux.

# How do I allow this to access my Twitter?

You need to register an "app" to your Twitter account, get consumer/access 
tokens and secrets, then put those keys into the configuration file. Then, 
we can start sending requests to the Twitter API.

# What's my Dota 2 ID?

You need to enable public match sharing so your name will come up in the 
Dota 2 JSON API. After that you can find your ID somewhere in the game's client, 
or you can log in through Steam on Dotabuff and find your profile directly.

# Why does this take so long to update?

Since Dotabuff is a free resource, it's best if we didn't spam it for
requests every two seconds. Dota matches typically last anywhere from
40 minutes to an hour, so the update is set to look up for new matches
every hour.

Plus if we continuously spammed Dotabuff, that's a good way to get
IP rate-limited by the site itself (if it doesn't already have
CloudFlare DOS protection). Let's just keep it nice and friendly.

# What's the inspiration behind this?

Simply because I couldn't find anything else that automatically posted
Dota 2 API info every time a match was completed. Within Dota 2 there
exists a kind of "Twitter" application but that data is only relevant
inside the client.

The Dota 2 API outputs a large feed of games completed, and even finding
one specific game that a player had played in that chunk would be astronomically
impossible without some kind of database. Services like Yasp and Dotabuff
graciously host all that info for us, so why not just simply carry that information
over to another website?

This is just designed as a fun little project.

# Credits

Here's the sites used:

* [Dotabuff](http://www.dotabuff.com/)
* [Twitter](https://twitter.com/)
