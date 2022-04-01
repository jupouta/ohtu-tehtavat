class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    def __str__(self):
        combined = self.goals + self.assists
        stringi = f"{self.name:20} {self.team} {self.goals:2} + {self.assists:2} = {combined:2}"
        return stringi
