import csv, string

#page = requests.get('https://rotogrinders.com/lineups/nba?site=fanduel')
#tree = html.fromstring(page.content)

#players = tree.xpath('//a[@class="player-popup"]/text()')
#print players

#prices = tree.xpath('//a')

#file_name = raw_input("list id: ")


# Read through available players from FanDuel player list file.
def get_player_list():
    file = open("FanDuel-NBA-2017-03-30-18476-players-list.csv")
    player_list = []
    reader = csv.reader(file)
    for row in reader:
        player = [row[1], row[2], row[4], row[7], row[9], row[10]]
        player_list.append(player)
    player_list.remove(player_list[0])
    return player_list

# Populate list of dictionary structures with player information
def get_dict_list():
    PLAYER_LIST = get_player_list()
    dict_list = []
    for i in PLAYER_LIST:
        dict_list.append({'NAME' : i[1].translate(None, string.punctuation)+" "+i[2].translate(None, string.punctuation), 'POS' : i[0], 'PRICE' : i[3], 'TEAM' : i[4], 'OPP' : i[5]})
        #print(i[1] + " " + i[2])
    return dict_list