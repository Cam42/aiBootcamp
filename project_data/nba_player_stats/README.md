Folder contains the NBA player salaries and statistics from "https://www.basketball-reference.com/leagues/NBA_"

basketball_data.py:
  program which obtains the data from "https://www.basketball-reference.com/leagues/NBA_" and puts it in the 2 csv files.  Takes advantage of the player stats pages over a season having the same format each year and the url only needing the year changed to get to that years' player stats.  Furthermore, the url for any player salary over their career is formatted so exchanging their name with any other player gets that players salary.  The relevant names were obtained from the season stats page with every player in the season having their unique name id included.

nba_player_salaries.csv :
  has 18360 lines formatted ['playerUrl', 'yearP', 'salaryP'] with each player having a datapoint for each year. 
 Starts in 1985 due to being when salary data was available.

nba_player_statistics.csv :
  has 22054 lines with player statistics starting in 1985.  Has more data points than nba_player_salaries.csv due to players having multiple data entries for a year if they were on multiple teams in a season or had multiple positions.
