'''
Program to obtain player statistics to put into nba_player_statistics.csv and player salaries to put into nba_player_salaries.csv from "https://www.basketball-reference.com/leagues/NBA_"
'''
import requests
import pandas as pd
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import time


def findYears() :
    '''
    gives site urls for every year player stats
    with player salaries given
    '''
    first = 1985  # first year salary stats are kept
    last = 2024
    # website url
    startStats = "https://www.basketball-reference.com/leagues/NBA_"
    # to get to all player stats in a season
    endStats = "_totals.html"
    urlSeasons = []
    
    for year in range(last, first - 1, -1) :

        seasonStats = startStats + str(year) + endStats
        urlSeasons.append(seasonStats)
        
    return urlSeasons

def findYearStats(yearUrl) :
    '''
    finds the stats for a season of NBA basketball
    '''
    # gets webpage html with season of player stats
    seasonData = urllib.request.urlopen(yearUrl)
    
    page = BeautifulSoup(seasonData, "html.parser")
    playerStats = [] # has lists with [playerUrl, ]
    playerUrls = [] # will have every playerUrl to check
    
    for link in page.find_all('a'):
        linkP = link.get('href')
        if linkP and '/players/' == linkP[:9] and len(linkP) > 10 :
            playerUrls.append(linkP)
    
    def tableDataText(table):    
        """
        for an html table gets the header row
        and rows with values
        """
        def rowgetDataText(tr, colTag='td'):     
            return [td.get_text(strip=True) for td in tr.find_all(colTag)]  
        
        tabelRows = []
        trs = table.find_all('tr')
        headerRow = rowgetDataText(trs[0], 'th')
        
        if headerRow:
            tabelRows.append(headerRow)
            trs = trs[1:]
        for tr in trs:
            tabelRows.append(rowgetDataText(tr, 'td') )  
        return tabelRows
        
    for link in page.find_all('div'):
        if link.get('id') == None : # to avoid None errors
            continue
        if 'div_totals_stats' == link.get('id') :

            playerStats = tableDataText(link)
            playerStats = [x for x in playerStats if x != list()]
       
    return playerStats, playerUrls
    


def findPlayerSalary(playerUrl="/players/a/adamsal01.html") :
    '''
    given the url of a player return a list with lists containing
    [the player url, year played, salary during year]
    '''
    siteUrl = "https://www.basketball-reference.com"
    
    playerData = urllib.request.urlopen(siteUrl + playerUrl)
    
    page = BeautifulSoup(playerData, "html.parser")
    playerSal = [] # has lists with [playerUrl, year, $salary]
    
    for link in page.find_all('div'):
        if link.get('id') == None : # to avoid None errors
            continue
        if 'all_all_salaries' == link.get('id') :

            for line in link :
                locId = line.find('div_all_salaries')
                if locId != None and locId != -1 :
                    for a in (line.split('tr ')[1:-1]) :
                        yearP = a[a.find('/leagues/NBA_') + 13: a.find('.html">NBA</a></td>')]
                        salaryP = a[a.find('csk="') + 5: a.find('" >$')]
                        if a.find('$') == -1 : # in case player salary is not listed
                            playerSal.append([playerUrl, yearP, 'NaN'])
                        else :
                            playerSal.append([playerUrl, yearP, salaryP])
    return playerSal
    

def main() :
    years = findYears()

    allPlyUrls = list()  # player urls
    # making pandas dataframe for player stats
    playerColumns = ['Player', 'Pos', 'Age', 'Tm', 'G',
            'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA',
            '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST',
            'STL', 'BLK', 'TOV', 'PF', 'PTS', 'year', 'url']
    dfPlayerStats = pd.DataFrame(columns=playerColumns)
    # making pandas dataframe for player salaries with year
    plSalCol = ['playerUrl', 'yearP', 'salaryP']
    dfPlayerSal = pd.DataFrame(columns=plSalCol)
    
    # gets the player stats for every year and turns it into a csv
    for year in years :
        listYearStats, listPlayerUrls = findYearStats(year)
        
        yearTable = pd.DataFrame(listYearStats[1:], columns=listYearStats[0][1:])
        listPlayerUrls = listPlayerUrls[6: 6 + yearTable.shape[0]] # to get only urls in table
        allPlyUrls += listPlayerUrls
        
        yLoc = year.find('_totals.html')
        yearTable['year'] = int(year[yLoc-4: yLoc])
        yearTable['url'] = listPlayerUrls
        dfPlayerStats = dfPlayerStats._append(yearTable)
        time.sleep(5) # to avoid HTTP Error 429: Too Many Requests
    dfPlayerStats.to_csv('./nba_player_statistics.csv')
    del dfPlayerStats
    # gets the player salaries for every year and turns it into a csv
    for playUrl in set(allPlyUrls) :
        playerSals = findPlayerSalary(playUrl)
        playerSals = pd.DataFrame(playerSals, columns=plSalCol)
        dfPlayerSal = dfPlayerSal._append(playerSals)
        
        time.sleep(5) # to avoid HTTP Error 429: Too Many Requests

    dfPlayerSal.to_csv('./nba_player_salaries.csv')

    return
    
main()

