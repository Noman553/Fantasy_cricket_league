class Player :
    def __init__(self , player_id,
                 player_name,
                 player_role,
                 player_franchise,
                 player_credits):
        self.player_id = player_id
        self.player_name = player_name
        self.player_role = player_role
        self.player_franchise = player_franchise
        self.player_credits = player_credits

    @classmethod
    def from_row(cls, row):
        """create the player object from the function"""
        return cls(
            row["player_id"],
            row["name"],
            row["role"],
            row["franchise"],
            float(row["credits"])
        )

class FantasyTeamLeague :
    def __init__(self, team_name,
                 owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None


    def add_player(self , player):
        self.players.append(player)

    def set_captains(self, captain, vice_captain ):
        self.captain = captain
        self.vice_captain = vice_captain
    def total_credits(self):
        return sum(player.player_credits for player in self.players)
    def count_by_role(self):
        counts={}
        for player in self.players:
            counts[player.player_role] = counts.get(player.player_role , 0) + 1
        return counts
    def count_by_franchise(self):
        counts={}
        for player in self.players:
            counts[player.player_franchise] = counts.get(player.player_franchise , 0) + 1
        return counts
    def check_rules(self):
        from noman_Dugout_league.rules import (
        check_players_count,
        check_budget,
        check_captain,
        check_duplicates,
        check_franchise_limit,
        check_roles
        )
        errors = []
        errors.extend(check_players_count(self))
        errors.extend(check_roles(self))
        errors.extend(check_franchise_limit(self))
        errors.extend(check_captain(self))
        errors.extend(check_budget(self))
        errors.extend(check_duplicates(self))

        return errors

class League :
    def __init__(self, name):
        self.name = name
        self.teams = {}
    def add_team(self, team):
        self.teams[team.owner] = team
    def find_team(self, owner):
        return self.teams.get(owner)
    def legal_team(self):
        return [
            team for team in self.teams.values()
            if not team.check_rules()
        ]
    def rank_teams(self):
        return sorted(
            self.teams.values(),
            key=lambda team: team.total_credits()
        )
