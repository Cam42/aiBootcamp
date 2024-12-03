Folder contains the NBA player salaries and statistics from "https://www.basketball-reference.com/leagues/NBA_"

basketball_data.py:
  program which obtains the data from "https://www.basketball-reference.com/leagues/NBA_" and puts it in the 2 csv files

nba_player_salaries.csv :
  has 18360 lines with ['playerUrl', 'yearP', 'salaryP'] with each player having a datapoint for each year.  Starts in 1985
  due to being when salary data was available.

nba_player_statistics.csv :
  has 22054 lines with player statistics starting in 1985.  Has more data points than nba_player_salaries.csv due to players having
  multiple data entries for a year if they were on multiple teams in a season or had multiple positions.
