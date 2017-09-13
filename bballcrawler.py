import csv

#page = requests.get('https://rotogrinders.com/lineups/nba?site=fanduel')
#tree = html.fromstring(page.content)

#players = tree.xpath('//a[@class="player-popup"]/text()')
#print players

#prices = tree.xpath('//a')

filename = raw_input("file: ")
file = open(filename)

def get_player_list():
    player_list = []
    reader = csv.reader(file)
    for row in reader:
        player = [row[1], row[4]+', '+row[2], row[7]]
        player_list.append(player)
    player_list.remove(player_list[0])
    return player_list

def get_sg_list():
    PLAYER_LIST = getPlayerList()
    two_guards = []
    for player in PLAYER_LIST:
        if player[0] == 'SG':
            two_guards.append([player[1],player[2]])
    return two_guards

def get_pg_list():
    PLAYER_LIST = getPlayerList()
    point_guards = []
    for player in PLAYER_LIST:
        if player[0] == 'PG':
            point_guards.append([player[1],player[2]])
    return point_guards

def get_sf_list():
    PLAYER_LIST = getPlayerList()
    small_forwards = []
    for player in PLAYER_LIST:
        if player[0] == 'SF':
            small_forwards.append([player[1],player[2]])
    return small_forwards

def get_pf_list():
    PLAYER_LIST = getPlayerList()
    power_forwards = []
    for player in PLAYER_LIST:
        if player[0] == 'PF':
            power_forwards.append([player[1],player[2]])
    return power_forwards

def get_c_list():
    PLAYER_LIST = getPlayerList()
    centers = []
    for player in PLAYER_LIST:
        if player[0] == 'C':
            centers.append([player[1],player[2]])
    return centers
