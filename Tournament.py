# The Tournament
winner = []
score = []

Continue = True
while Continue == True:

    team_name = input("Team Name? ")
    opposers = input("Another Team? ")
    team_score = int(input("Your Team's Score? "))
    other_teams_score = int(input("Opposing Teams Score? "))

    Again = input("Do you want to enter another round? y/n  ")
    if Again == "n":
        Continue = False
        print("ok")

else:
    score.append(team_score)
    if team_score > score:
        score = team_score
        winner = name
    Again = input("Do you want to enter another round? y/n  ")
    if Again == "n":
        Continue = False
        print("ok")
print("Highest Bidding Price is: ${} made by {}".format(max_bid, leader))
