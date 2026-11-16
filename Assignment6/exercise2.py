seasons = ("spring", "summer", "autumn", "winter")

month = int(input("Enter the number of a month: "))

if month == 1 or month == 2 or month == 3:
    season = seasons[0]
elif month == 4 or month == 5 or month == 6:
    season = seasons[1]
elif month == 7 or month == 8 or month == 9:
    season = seasons[2]
else:
    season = seasons[3]

print("The season is", season)