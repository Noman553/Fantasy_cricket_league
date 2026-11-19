#let's define league rules
TEAM_SIZE = 11
MAX_CREDITS = 100
MAX_FROM_EACH_FRANCHISE = 7

ROLE_LIMITS = {
    "WK" : (1 , 2),
    "BAT": (3 , 5),
    "BOWL":(3 , 5),
    "AR" : (1 , 3)
}

def check_players_count(team):
    error = []
    if len(team.players) != TEAM_SIZE:
        error.append(
            f"You must have {TEAM_SIZE} players in your team"
        )
    return error

def check_budget(team):
    errors = []
    if team.total_credits() > MAX_CREDITS :
        errors.append(
            f"Team budget exceeded: {team.total_credits()} / {MAX_CREDITS}"
        )
    return errors

def check_franchise_limit(team):
    errors = []
    franchise_counts = team.count_by_franchise()
    for franchise , count in franchise_counts.items() :
        if count > MAX_FROM_EACH_FRANCHISE:
            errors.append(
                f"{franchise} has {count} Players . Maximum Allowed is {MAX_FROM_EACH_FRANCHISE}"
            )
    return errors

def check_roles(team):
    errors = []
    count_role = team.count_by_role()
    for role, (minimum , maximum) in ROLE_LIMITS.items():
        count = count_role.get(role, 0)
        if count < minimum or count > maximum :
            errors.append(
                f"{role} must have between {minimum} and {maximum} players . Found{count}"
            )
    return errors

def check_captain(team):
    errors = []
    if team.captain is None :
        errors.append(
            "The captain has not been selected"
        )
    if team.vice_captain is None:
        errors.append(
            "The vice Captain has not been selected"
        )
    if team.captain is not None and team.captain not in team.players:
        errors.append(
            "The Captain is not in team"
        )
    if team.vice_captain is not None and team.vice_captain not in team.players:
        errors.append(
            "The Vice Captain is not in team"
        )
    if (
        team.captain is not None
        and team.vice_captain is not None
        and team.captain == team.vice_captain
    ):
        errors.append(
            "The Captain and Vice Captain must be different players."
        )
    return errors
def check_duplicates(team):
    errors = []
    seen_players = set()
    for player in team.players:
        if player.player_id in seen_players:
            errors.append(
                f"Duplicate Players found : {player.player_name}"
            )
        else:
            seen_players.add(player.player_id)
    return errors
