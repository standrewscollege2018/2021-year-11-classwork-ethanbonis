##### Alternative approach ######
# Start by creating an empty list for all the opposing teams to go into
opponents = []

# Set the number of competition points the team has
points = 0

# Next, get the name of your team
team_name = input("Team name?")
# Now start a loop that keeps asking for the names of the opposing teams, adding to them to the opponents list. When user enters done, the loop ends
get_opponent = True
while get_opponent == True:
    opponent = input("Opponent name:")
    # Check if user is done
    if opponent == "done":
        get_opponent = False
    else:
        # Append name of opponent to the list of opponents
        opponents.append(opponent)

# Now that the program is finished asking for opponents, start looping through the list of opponents and get the scores
for team in opponents:
    print("Match vs {}".format(team))
    # Get your score
    
    # Get the opponent's score
    
    # Calculate points (3 fora win, 2 for a draw, 1 for a loss)
    # I just did the win, you need to write code for the draw and loss
    if score > opponent_score:
        points += 3
        
# Finally, once the program finishes looping through the list of opponents, it means we have entered all of the results.
# Now, you just finish by displaying how many points the team finished with
print("{} finished with {} points".format(team_name, points))
        
##### This is your original code ##### 
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
