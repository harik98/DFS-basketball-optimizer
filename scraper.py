from lxml import html
from lxml import etree
import requests
import private
import csv
import playerlists

#players = playerlists.get_dict_list()
headerFile = "header.txt"
startOfRow = '<th scope='
endOfRow = '</tr>'

def get_defense_vs_pg():
    page = requests.get('https://www.rotowire.com/daily/nba/defense-vspos.php?site=FanDuel&statview=last5')
    tree = html.fromstring(page.content)
    data = tree.xpath('//td/text()')
    names = []
    defense = []
    pg_defense = {}
    for i in range(len(data)):
        if i % 14 == 3:
            defense.append(data[i])
        elif i % 14 == 0:
            if data[i] == 'Golden State Warriors':
                names.append('GS')
            elif data[i] == 'New York Knicks':
                names.append('NY')
            elif data[i] == 'Brooklyn Nets':
                names.append('BKN')
            elif data[i] == 'San Antonio Spurs':
                names.append('SA')
            elif data[i] == 'Los Angeles Clippers':
                names.append('LAC')
            elif data[i] == 'Los Angeles Lakers':
                names.append('LAL')
            elif data[i] == 'Oklahoma City Thunder':
                names.append('OKC')
            elif data[i] == 'New Orleans Pelicans':
                names.append('NO')
            else:
                names.append(data[i][0:3].upper())
    for i in range(len(names)):
        pg_defense[names[i]] = defense[i]
    return pg_defense

def get_defense_vs_sg():
    page = requests.get('https://www.rotowire.com/daily/nba/defense-vspos.php?site=FanDuel&statview=last5&pos=SG')
    tree = html.fromstring(page.content)
    data = tree.xpath('//td/text()')
    names = []
    defense = []
    sg_defense = {}
    for i in range(len(data)):
        if i % 14 == 3:
            defense.append(data[i])
        elif i % 14 == 0:
            if data[i] == 'Golden State Warriors':
                names.append('GS')
            elif data[i] == 'New York Knicks':
                names.append('NY')
            elif data[i] == 'Brooklyn Nets':
                names.append('BKN')
            elif data[i] == 'San Antonio Spurs':
                names.append('SA')
            elif data[i] == 'Los Angeles Clippers':
                names.append('LAC')
            elif data[i] == 'Los Angeles Lakers':
                names.append('LAL')
            elif data[i] == 'Oklahoma City Thunder':
                names.append('OKC')
            elif data[i] == 'New Orleans Pelicans':
                names.append('NO')
            else:
                names.append(data[i][0:3].upper())
    for i in range(len(names)):
        sg_defense[names[i]] = defense[i]
    return sg_defense

def get_defense_vs_sf():
    page = requests.get('https://www.rotowire.com/daily/nba/defense-vspos.php?site=FanDuel&statview=last5&pos=SF')
    tree = html.fromstring(page.content)
    data = tree.xpath('//td/text()')
    names = []
    defense = []
    sf_defense = {}
    for i in range(len(data)):
        if i % 14 == 3:
            defense.append(data[i])
        elif i % 14 == 0:
            if data[i] == 'Golden State Warriors':
                names.append('GS')
            elif data[i] == 'New York Knicks':
                names.append('NY')
            elif data[i] == 'Brooklyn Nets':
                names.append('BKN')
            elif data[i] == 'San Antonio Spurs':
                names.append('SA')
            elif data[i] == 'Los Angeles Clippers':
                names.append('LAC')
            elif data[i] == 'Los Angeles Lakers':
                names.append('LAL')
            elif data[i] == 'Oklahoma City Thunder':
                names.append('OKC')
            elif data[i] == 'New Orleans Pelicans':
                names.append('NO')
            else:
                names.append(data[i][0:3].upper())
    for i in range(len(names)):
        sf_defense[names[i]] = defense[i]
    return sf_defense

def get_defense_vs_pf():
    page = requests.get('https://www.rotowire.com/daily/nba/defense-vspos.php?site=FanDuel&statview=last5&pos=PF')
    tree = html.fromstring(page.content)
    data = tree.xpath('//td/text()')
    names = []
    defense = []
    pf_defense = {}
    for i in range(len(data)):
        if i % 14 == 3:
            defense.append(data[i])
        elif i % 14 == 0:
            if data[i] == 'Golden State Warriors':
                names.append('GS')
            elif data[i] == 'New York Knicks':
                names.append('NY')
            elif data[i] == 'Brooklyn Nets':
                names.append('BKN')
            elif data[i] == 'San Antonio Spurs':
                names.append('SA')
            elif data[i] == 'Los Angeles Clippers':
                names.append('LAC')
            elif data[i] == 'Los Angeles Lakers':
                names.append('LAL')
            elif data[i] == 'Oklahoma City Thunder':
                names.append('OKC')
            elif data[i] == 'New Orleans Pelicans':
                names.append('NO')
            else:
                names.append(data[i][0:3].upper())
    for i in range(len(names)):
        pf_defense[names[i]] = defense[i]
    return pf_defense

def get_defense_vs_c():
    page = requests.get('https://www.rotowire.com/daily/nba/defense-vspos.php?site=FanDuel&statview=last5&pos=C')
    tree = html.fromstring(page.content)
    data = tree.xpath('//td/text()')
    names = []
    defense = []
    c_defense = {}
    for i in range(len(data)):
        if i % 14 == 3:
            defense.append(data[i])
        elif i % 14 == 0:
            if data[i] == 'Golden State Warriors':
                names.append('GS')
            elif data[i] == 'New York Knicks':
                names.append('NY')
            elif data[i] == 'Brooklyn Nets':
                names.append('BKN')
            elif data[i] == 'San Antonio Spurs':
                names.append('SA')
            elif data[i] == 'Los Angeles Clippers':
                names.append('LAC')
            elif data[i] == 'Los Angeles Lakers':
                names.append('LAL')
            elif data[i] == 'Oklahoma City Thunder':
                names.append('OKC')
            elif data[i] == 'New Orleans Pelicans':
                names.append('NO')
            else:
                names.append(data[i][0:3].upper())
    for i in range(len(names)):
        c_defense[names[i]] = defense[i]
    return c_defense

def getInitialPath(stat):
    return '//th[@class="right "][@data-stat="' + stat + '"]/text()'

def getPath(stat):
    return '//td[@data-stat="' + stat + '"]//text()'

def getUrl(first_name, last_name, year, num):
    return 'http://www.basketball-reference.com/players/' + last_name[0] + '/' + last_name[:5] + first_name[:2] + num + '/gamelog/' + str(year) + '/'

def condensePage(page):
    index_of_start = page.find(startOfRow)
    index_of_end = page.rfind(endOfRow)
    return page[index_of_start:index_of_end]
    
def getStatsForPlayer(playerName, year):
    num = 1
    if(playerName.lower() == 'larry nance jr'):
        playerName = 'larry nance'
    if(playerName.lower() == 'derrick jones jr'):
        playerName = 'derrick jones'
    if(playerName.lower() == 'luc richard mbah a moute'):
        playerName = 'luc mbaha'
    if(playerName.lower() == 'metta world peace'):
        playerName = 'ron artest'
    nameArr = playerName.split(' ')
    firstName = nameArr[0].lower()
    lastName = nameArr[1].lower()
    if(lastName == 'capela'):
        firstName = 'capela'
    #print firstName + ' ' + lastName
    if (len(nameArr) > 2):
        num = int(nameArr[2])

    foundPlayer = False
    keepLooping = True
    # Retrieve the HTML page in a condensed form
    while foundPlayer == False:
        urlStr = private.getURL(firstName, lastName, year, "0" + str(num))
        try:
            condensedPage = condensePage(requests.get(urlStr).content)
        except requests.exceptions.ConnectionError:
            print "Cannot Connect.\n"
            exit()
        try:
            tree = html.fromstring(condensedPage)
        except etree.XMLSyntaxError:
            num+=1
            if num == 5:
                print "Player " + playerName + " Not Found.\n"
                exit()
        else:
            foundPlayer = True


    # Retrieve the two forms of headers 
    file = open(headerFile)
    tableHeadersStr = file.readline()
    dataStatsStr = file.readline()
    tableHeaders = tableHeadersStr.replace(" ", "").strip().split(',')
    dataStats = dataStatsStr.replace(" ", "").strip().split(',')

    gameStats = []

    # Get number of games
    tempPath = private.getInitialPath(dataStats[0])
    numGames = len(tree.xpath(tempPath))

    # Traverse through games and retrieve all data
    lastIndex = 0
    rk = 1
    for count in range(0, numGames):
        dict = {}
        i = 0
        if condensedPage.find(startOfRow, lastIndex+len(startOfRow)) == -1:
            thisRow = condensedPage[lastIndex:]
        else:
            thisRow = condensedPage[lastIndex:condensedPage.find(startOfRow, lastIndex+len(startOfRow))]
        lastIndex = condensedPage.find(startOfRow, lastIndex+len(startOfRow))
        tree = html.fromstring(thisRow)
        for datastat in dataStats:
            if (datastat == 'ranker'):
                thisData = [str(rk)]
            else:
                xpathStr = private.getPath(datastat)
                thisData = tree.xpath(xpathStr)
            if (len(thisData) == 1):
                dict[tableHeaders[i]] = thisData[0]
            else:
                dict[tableHeaders[i]] = "N/A"
            i+=1
        dict['NAME'] = playerName.upper() # provides easy access to player's name
        dict['TITLE'] = "" # for titling purposes
        gameStats.append(dict)
        rk+=1

    #for s in gameStats:
    #	print s
    #	print
    return gameStats