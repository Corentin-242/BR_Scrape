# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:19:37 2023

@author: colos
"""


with open('games_links_202021.txt', 'r') as f:
    file = f.readlines()
    
with open('proper_games_links_202021.txt', 'w') as f:
        
    for x in file:
        result = x.split('/')
        result = f'boxscore/{result[-1]}'
        f.write(result)

with open('games_links_202122.txt', 'r') as f:
    file = f.readlines()
    
with open('proper_games_links_202122.txt', 'w') as f:
        
    for x in file:
        result = x.split('/')
        result = f'boxscore/{result[-1]}'
        f.write(result)


with open('games_links_202223.txt', 'r') as f:
    file = f.readlines()
    
with open('proper_games_links_202223.txt', 'w') as f:
        
    for x in file:
        result = x.split('/')
        result = f'boxscore/{result[-1]}'
        f.write(result)
