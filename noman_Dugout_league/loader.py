import csv
from noman_Dugout_league.model import FantasyTeamLeague , Player

def load_player(path):
    players = {}
    with open(path, newline="", encoding="UTF-8") as file:
        for row in csv.DictReader(file):
            player = Player.from_row(row)
            players[player.player_id] = player
    return players

def team_from_row(players , row):
    team = FantasyTeamLeague(row["team_name"].strip(),
                             row["owner"].strip())
    for player_id in row["players"].split(";"):
        team.add_player(players[player_id.strip()])
    team.set_captains(
        players[row["captain"].strip()],
        players[row["vice_captain"].strip()],
    )
    return team

def load_team(path, players):

    """load the team form the csv file"""
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            return team_from_row(players, row)
    return None

def load_teams(path ,players):
    """load multiple team form csv"""
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        print("HEADERS:", reader.fieldnames)

        teams = []

        for row in reader:
            print("ROW:", row)
            team = team_from_row(players, row)
            teams.append(team)
    return teams



