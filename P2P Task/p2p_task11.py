teams = {}

while True:
    name = input("Enter team name (or 'exit' to stop): ")
    if name == "exit":
        break
    wins = int(input("Enter number of wins: "))
    loss = int(input("Enter number of losses: "))
    teams[name] = [wins, loss]

team_name = input("Enter team name to check winning percentage: ")
team_record = teams.get(team_name)
if team_record:
    total_games = team_record[0] + team_record[1]
    win_percent = (team_record[0] / total_games) * 100
    print(f"{team_name} winning percentage: {win_percent:.2f}%")
else:
    print(f"{team_name} not found in dictionary.")

wins_list = [team[0] for team in teams.values()]

winning_teams = [team for team in teams if teams[team][0] > teams[team][1]]

print("List of wins for all teams:", wins_list)
print("List of teams with winning records:", winning_teams)

