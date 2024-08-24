
day = int(input("Enter the day of the week (1 for Monday, 2 for Tuesday, etc.): "))
hour = int(input("Enter the hour of the day (24-hour format): "))


opening_hour = 10
closing_hour = 21

if 1 <= day <= 7 and 0 <= hour <= 23:
    # Check if the store is open
    if 1 <= day <= 7 and opening_hour <= hour < closing_hour:
        print("The store is open.")
    else:
        print("The store is closed.")
else:
    print("Invalid input.")