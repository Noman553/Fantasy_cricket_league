from noman_Dugout_league.loader import load_player , load_teams
from noman_Dugout_league.model import League

players = load_player("./noman_Dugout_league/dugout_starter/data/players.csv")

teams = load_teams("./noman_Dugout_league/dugout_starter/data/sample_teams.csv",
                   players)

my_teams = load_teams("./noman_Dugout_league/dugout_starter/data/my_team.csv",
                      players)
combined_team = teams + my_teams

for team in teams:
    print(f"\n Team: {team.team_name}")
    errors = team.check_rules()
    if errors:
        print("Status : illegal")
        for error in errors:
            print("_" , error)
    else:
        print("Status : legal ")
for my_team in my_teams:
    print("\n My team" , my_team.team_name)
    errors = my_team.check_rules()
    if errors :
       print("Status : illegal")
    for error in errors:
        print("_", error)
    else :
      print("Status : legal")

def show_team(team):
    print("========My Team===========")
    print("Team Name:", team.team_name)
    print("Team Owner:", team.owner)

    print("\n Players:")
    for player in team.players:
        print(
            player.player_name,
            "|",player.player_role,
            "|",player.player_franchise,
            "|",player.player_credits
        )
    print("\n Captain:" , team.captain.player_name)
    print(" Vice Captain:", team.vice_captain.player_name)
    total = team.total_credits()
    print(" Total credits:", total)
    print("Remaining Credits:", 100 - total )
    new_errors =team.check_rules()
    if new_errors:
        print("Status Illegal")
        for new_error in new_errors:
            print("_" , new_error)
        else:
            print("Status legal:")
for new_team in my_teams:
    show_team(new_team)
print("\nTotal Players:", len(players))
print("Sample Teams:", len(teams))

league = League("Fantasy Cricket League")

for team in combined_team:
    league.add_team(team)
print("\n=========== LEAGUE INFORMATION =============")
print("League Name:", league.name)
print("Total Teams:", len(league.teams))

print("\n========== TEAM RANKING ================")

ranked_team = league.rank_teams()

for position , team in enumerate(ranked_team, start=1) :
    print(
        position,
        team.team_name,
        "| Owner:", team.owner,
        "| Credits:", team.total_credits()

    )

