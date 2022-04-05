import requests

def sorted_points(player):
    result = player.goals + player.assists
    return result

class Player:
    def __init__(self, name, team, goals, assists, nationality):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.nationality = nationality

    def __str__(self):
        combined = self.goals + self.assists
        stringi = f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {combined:2}"
        return stringi

class PlayerReader:

    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict['nationality']
            )

            players.append(player)
        return players

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        sorted_players = sorted(self.reader.players, reverse=True, key=sorted_points)

        result = []

        for player in sorted_players:
            if player.nationality == nationality:
                result.append(player)
        return result