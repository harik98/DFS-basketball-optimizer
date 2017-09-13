import playerlists
import scraper

def complete_list():
    player_list = playerlists.get_dict_list()
    valid = True
    #print player_list
    for player in player_list:
        print "Getting data for " + player['NAME']
        last_10 = []
        player_stats = scraper.getStatsForPlayer(player['NAME'], 2017)
        #print player_stats
        index = 1
        first_game = player_stats[len(player_stats)-index]
        while first_game['MP'] == 'N/A':
            index += 1
            if(len(player_stats)-index < 0):
                last_10 = "Not a viable player"
                valid = False
                break
            first_game = player_stats[len(player_stats)-index]
            #print first_game['MP']
            #first_min = int(first_game['MP'].split(':')[0] )# + (int(first_game['MP'].split(':')[1])/60.0)
        if(valid):
            first_min = int(first_game['MP'].split(':')[0] )# + (int(first_game['MP'].split(':')[1])/60.0)
            #print first_game
            while first_min < 20:
                index += 1
                if(len(player_stats)-index < 0):
                    last_10 = "Not a viable player"
                    valid = False
                    break
                first_game = player_stats[len(player_stats)-index]
                if first_game['MP'] != 'N/A':
                    first_min = int(first_game['MP'].split(':')[0]) # + .01*int(first_game['MP'].split(':')[1]
        if(valid):
            last_10.append(first_game)
            game = player_stats.index(first_game)-1
            #print game
            while game >= 0 and len(last_10) < 10:
                curr_game = player_stats[game]
                #print curr_game
                if curr_game['MP'] != 'N/A':
                    minutes = int(curr_game['MP'].split(':')[0]) # + .01*int(curr_game['MP'].split(':')[1])
                    if minutes >= 20:
                        last_10.append(curr_game)
                    game -= 1
                else:
                    game -= 1
        player['GAMES'] = last_10
        #print last_10[9]
    return player_list

def get_position(player_list, pos):
    pos_list = []
    for player in player_list:
        if player['POS'] == pos and len(player['GAMES']) > 0:
            pos_list.append(player)
    return pos_list

print get_position(complete_list(), 'PG')
    

