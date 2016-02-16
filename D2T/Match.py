#!/usr/bin/env python
#-*- coding: utf-8 -*-

from .Utils import parse_id, parse_stat, parse_hero, PStat, Match
from collections import namedtuple
from requests import get as re_get
from bs4 import BeautifulSoup

# assemble some NTs based on Dotabuff's structs
# radiant and dire are lists of players (using the PSTat nt)
def to_pstat(row):
    '''
    Convert a <tr> player row to a PStat row

    Values:
    elem = (all <td> elements in the row)
    hero = elem[0] + some extraction
    name/id = elem[1] + some extraction
    numbers = elem[3:] + some converting types
    '''
    # elem[0] is the Hero pic - use this to find Hero
    # elem[1] is the User name - either real or Anonymous
    # everything from elem3 and onwards is a corresponding PStat value
    # PStat.name == elem[1], PStat.everything_else = elem[3:]
    # If elem[1] has an <a> tag, the player linked their profile and 
    # the name is contained inside an <a> tag instead
    # else, the name is Anonymous so no need to fetch any further
    # If possible, extract the User ID from linked profiles
    # In PStat, if a player is Anon, just make it None
    tds = row.find_all('td')

    # Find the hero pic and extract a name from the URI
    hero_row = tds[0]
    hero_a   = hero_row.find('a')
    hero = parse_hero(hero_a.get('href'))

    # Find the player name (either real or Anonymous)
    # Also find ID if possible (set to zero if no ID)
    name_row = tds[1]
    a_link   = name_row.find('a', class_='link-type-player')
    if a_link:
        # Name was found
        name = a_link.text
        pid = parse_id(a_link.get('href'))
    else:
        # It's anonymous
        name = "Anonymous"
        pid  = 0

    # Parse the numbers from this shit
    nums = [parse_stat(x.text) for x in tds[3:]]
    return PStat(pid, name, hero, *nums)

def get_match(mid):
    '''
    '''
    if not isinstance(mid, int):
        raise Exception("Invalid Match ID type given")

    s   = "http://www.dotabuff.com/matches"
    uri = "/".join([s, str(mid)])
    doc = re_get(uri, headers={'User-Agent':'Mozilla/5.0'})
    bs  = BeautifulSoup(doc.text, 'html.parser')

    # Get the winning team
    winner = bs.find('div', class_='match-result').text.split(' ').pop(0)

    # Get the player rows
    radi_rows = bs.find_all('tr', class_='faction-radiant')
    dire_rows = bs.find_all('tr', class_='faction-dire')

    # Convert the rows into PStats for the teams
    radi_team = [to_pstat(row) for row in radi_rows]
    dire_team = [to_pstat(row) for row in dire_rows]
    return Match(mid, radi_team, dire_team, winner) 

def test_match():
    print("Testing match 2152894897")
    m = get_match(2152894897)
    print(m.victor)
    print("Radiant team:")
    for x in m.radiant:
        print(x)
    print("Dire team:")
    for x in m.dire:
        print(x)
