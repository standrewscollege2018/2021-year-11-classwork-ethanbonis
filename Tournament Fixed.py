

#### Alternative approach ######
# Start by creating an empty list for all the opposing teams to go into
opponents = []

# Set the number of competition points the team has
points = 0

# Next, get the name of your team
why_not = True
while why_not == True:
    team_name = input("Team name?")
    if team_name.replace(" ", "") == "":
        print("Enter a proper name")
    else:
        why_not = False
# Now start a loop that keeps asking for the names of the opposing teams, adding to them to the opponents list. When user enters done, the loop ends
get_opponent = True
while get_opponent == True:
    opponent = input("Opponent name:")
    # check if empty
    if opponent.replace(" ", "") == "":
        print("Enter a proper name")
    # Check if user is done
    elif opponent == "done":
        get_opponent = False
    else:
        # Append name of opponent to the list of opponents
        opponents.append(opponent)

# Now that the program is finished asking for opponents, start looping through the list of opponents and get the scores
for team in opponents:
    print("Match vs {}".format(team))
    # Get your score
    score = int(input("Score of team:"))
    # Get the opponent's score
    opponent_score = int(input("Score of opponents team:"))
    # Calculate points (3 for a win, 2 for a draw, 1 for a loss)
    # I just did the win, you need to write code for the draw and loss
    if score > opponent_score:
        points += 3
    elif score < opponent_score:
        points += 1
    else:
        points += 2

# Finally, once the program finishes looping through the list of opponents, it means we have entered all of the results.
# Now, you just finish by displaying how many points the team finished with
print("{} finished with {} points".format(team_name, points))

##### This is your original code #####
# The Tournament
winner = []
score = []
