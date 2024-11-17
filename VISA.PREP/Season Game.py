month = int(input())
seasons = {
    "Spring": range(3, 6),
    "Summer": range(6, 9),
    "Autumn": range(9, 12),
    "Winter": ([12] + list(range(1, 3)))
}
for season, months in seasons.items():
    if month in months:
        print(season)
        break
else:
    print("Invalid")
