import unittest

target = __import__("tournament_winner")

class TestTournamentWinner(unittest.TestCase):
    def test_case_1(self):
        competitions = [["a","b"]]
        results = [1]
        winner = target.tournament_winner(competitions, results)
        self.assertEqual(winner, "a")

    def test_case_2(self):
        competitions = [["a","b"]]
        results = [0]
        winner = target.tournament_winner(competitions, results)
        self.assertEqual(winner, "b")

    def test_case_3(self):
        competitions = [["a","b"],["a","c"],["b","c"]]
        results = [1,1,0]
        winner = target.tournament_winner(competitions, results)
        self.assertEqual(winner, "a")

    def test_case_4(self):
        competitions = [["a","b"],["a","c"],["b","c"]]
        results = [1,0,1]
        winner = target.tournament_winner(competitions, results)
        self.assertIn(winner, ["a","b","c"])
        

if __name__ == '__main__':
    unittest.main()
