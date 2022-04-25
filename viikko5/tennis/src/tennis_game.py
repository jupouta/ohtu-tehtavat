MINUS_RESULT = 4
SCORE_LOWER = 1
SCORE_UPPER = 3

temp_score_dict = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"
}

score_dict = {
    0: "Love-All",
    1: "Fifteen-All",
    2: "Thirty-All",
    3: "Forty-All"
}


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score1 = 0
        self.p2_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score1 += 1
        else:
            self.p2_score2 += 1

    def get_score_results(self):
        score_lambda = lambda x : score_dict[x] if x in score_dict else "Deuce"
        return score_lambda(self.p1_score1)

    def get_minus_results(self, score):
        minus_result = self.p1_score1 - self.p2_score2

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def get_score(self):
        score = ""
        temp_score = 0

        if self.p1_score1 == self.p2_score2:
            score = self.get_score_results()

        elif self.p1_score1 >= MINUS_RESULT or self.p2_score2 >= MINUS_RESULT:
            score = self.get_minus_results(score)

        else:
            for i in range(SCORE_LOWER, SCORE_UPPER):
                if i == SCORE_LOWER:
                    temp_score = self.p1_score1
                else:
                    score = score + "-"
                    temp_score = self.p2_score2

                score = score + temp_score_dict[temp_score]

        return score
