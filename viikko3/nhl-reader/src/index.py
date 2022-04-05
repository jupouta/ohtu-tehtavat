from player import PlayerReader, PlayerStats

# {'name': 'Antti Suomela',
# 'nationality': 'FIN',
# 'assists': 0,
# 'goals': 0,
# 'penalties': 0,
# 'team': 'SJS',
# 'games': 4}

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
