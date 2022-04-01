import requests
from player import Player

# {'name': 'Antti Suomela',
# 'nationality': 'FIN',
# 'assists': 0,
# 'goals': 0,
# 'penalties': 0,
# 'team': 'SJS',
# 'games': 4}

def sorted_points(player):
    result = player.goals + player.assists
    return result


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    print("Oliot:")

    sorted_players = sorted(players, reverse=True, key=sorted_points)

    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()
