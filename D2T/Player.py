#!/usr/bin/env python
#-*- coding: utf-8 -*-

from .Utils import parse_hero, parse_id, Player
from collections import namedtuple
from requests import get as re_get
from bs4 import BeautifulSoup

def get_player(pid=0):
    '''
    Create a Player tuple from an ID
    Request the Dotabuff, join the ID and scan the page with BS4
    '''
    if not isinstance(pid, int):
        raise Exception("Invalid Player ID type given")

    s   = "http://www.dotabuff.com/players"
    uri = "/".join([s, str(pid)])
    doc = re_get(uri, headers={'User-Agent':'Mozilla/5.0'})
    bs  = BeautifulSoup(doc.text, 'html.parser')
    pnm = bs.title.string.split(" ").pop(0) # should fetch the player's Name

    # row finding block
    rws = bs.find_all('div', class_='r-row')

    # first 10  have to retrieve a-href URIs
    hrs = [parse_hero(x.find('a').get('href')) for x in rws[:10]]

    # fetch match URIs after the 10th row
    mts = [parse_id(h.get('data-link-to')) for h in rws[10:]]

    # finish
    return Player(pid, pnm, hrs, mts)


def test_player():
   print("Testing player 40281889")
   steve = get_player(40281889)
   print(steve.name)

