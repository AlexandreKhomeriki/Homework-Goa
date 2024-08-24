
wins = input("Enter the number of wins: ")
ties = input("Enter the number of ties: ")

wins = float(wins)
ties = float(ties)


points_from_wins = wins * 1  
points_from_ties = ties * 0.5  

total_points = points_from_wins + points_from_ties

print(f"Total points earned: {total_points}")