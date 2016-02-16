#!/usr/bin/env python
#-*- coding: utf-8 -*-

from collections import namedtuple

# Named Tuples to use across the project
# Player corresponds to a Player's profile page
# Match corresponds to a Match page
# PStat is the Player Stats within a Match page (used within Match)
Player = namedtuple("Player", ["id", "name", "heroes", "matches"])
Match = namedtuple("Match", ["id", "radiant", "dire", "victor"])
PStat = namedtuple("PStat", ["id", "name", "hero", "lvl", "kills", "deaths", 
                             "assists", "kda", "gold", "lh", "dn", "xpm", 
                             "gpm", "hd", "hh", "td", "items"])

def parse_id(id_str):
    '''
    Parse an ID to be an int instead of a link
    '''
    if not isinstance(id_str, str):
        raise Exception("Invalid ID type given")
    return int(id_str.split("/").pop())

def parse_stat(int_str):
    '''
    Parse a string into an integer
    If it can't become a string, return the argument
    '''
    if not isinstance(int_str, str):
        raise Exception("Wrong value type given to parse_stat")
    if int_str.strip() == "-": # for null values (DB stores empty as "-")
        return 0
    if int_str.isnumeric():
        return int(int_str)
    return int_str

def parse_hero(hero_uri):
    '''
    Parse a Hero URI into a string with capitalized words
    '''
    new = hero_uri.split('/').pop().split('-')
    caps = [x.capitalize() for x in new]
    return " ".join(caps)

