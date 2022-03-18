import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_works(self):
        player = self.statistics.search('Semenko')
        self.assertIsNotNone(player)

        player = self.statistics.search('Rantanen')
        self.assertIsNone(player)

    def test_team_works(self):
        team = self.statistics.team('EDM')
        self.assertEqual(len(team), 3)

        team = self.statistics.team('PIT')
        self.assertEqual(len(team), 1)

        team = self.statistics.team('PHI')
        self.assertEqual(len(team), 0)

    def test_top_scorers_works(self):
        result = self.statistics.top_scorers(4)
        self.assertEqual(len(result), 5)

        result = self.statistics.top_scorers(3)
        self.assertEqual(len(result), 4)