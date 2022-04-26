from matchers import *

class QueryBuilder:
    def __init__(self, olio = All()):
        self.query_olio = olio

    def playsIn(self, team):
        return QueryBuilder(And(self.query_olio, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_olio, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_olio, HasFewerThan(value, attr)))

    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1, query2))

    def build(self):
        return self.query_olio