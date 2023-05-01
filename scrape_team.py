from time import sleep
import re, os, requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm
URL = 'https://www.basketball-reference.com/teams/'

def get_page():
    response = requests.get(URL)
    html = bs(response.content,'html.parser')
    return(html)

def get_team_abrv():
    html = get_page()
    teams = []
    divisions = html.find_all("div", class_="division")
    print(divisions)
    for i, division in enumerate(divisions):
        teams_links = divisions[i].find_all('a')
        for team in teams_links:
            team_link = team.get('href')
            abrv = team_link.split('/')[2]
            teams.append(abrv)
    return(teams)
        
TEAMS = get_team_abrv()

def get_links_games_team(team,season):
    url = f'https://www.basketball-reference.com/teams/{team}/{season}_games.html'
    return(url)

def get_games_team(team,season):
    games_id = []
    url = get_links_games_team(team,season)
    response = requests.get(url)
    html = bs(response.content,'html.parser')
    games_box_score = html.find_all(text='Box Score')
    for game_box_score in games_box_score:
        games_link = game_box_score.parent.get('href')
        print(games_link)
        game_id = games_link.split('/')[2]
        games_id.append(game_id)
        
    return(games_id)

def get_pbp_link(season):
    links = set()
    for team in tqdm(TEAMS):
        sleep(10)
        games_id = get_games_team(team,season)
        for game_id in tqdm(games_id, position=0, leave=True): 
            url = f'https://www.basketball-reference.com/boxscores/pbp/{game_id}'
            if url not in links:
                links.add(url)
    return(links)

LINKS_202021 = get_pbp_link(2021)
LINKS_202122 = get_pbp_link(2022)
LINKS_202223 = get_pbp_link(2023)


LINKS_l_202021 = list(LINKS_202021)

with open('games_links_202021.txt', 'w') as f:
    f.write('\n'.join(LINKS_l_202021))
    

LINKS_l_202122 = list(LINKS_202122)

with open('games_links_202122.txt', 'w') as f:
    f.write('\n'.join(LINKS_l_202122))
    
LINKS_l_202223 = list(LINKS_202223)

with open('games_links_202223.txt', 'w') as f:
    f.write('\n'.join(LINKS_l_202223))
    

