import unittest
from HumanMoveTest.runner_and_tournament import Runner, Tournament
def frozen_test(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @frozen_test
    def test_tournament_usain_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        results = tournament.start()
        self.assertTrue(results[max(results)] == "Ник")

    @frozen_test
    def test_tournament_andrey_nik(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        results = tournament.start()
        self.assertTrue(results[max(results)] == "Ник")

    @frozen_test
    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.assertTrue(results[max(results)] == "Ник")


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @frozen_test
    def test_tournament_usain_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        results = tournament.start()
        self.assertTrue(results[max(results)] == "Ник")

    @frozen_test
    def test_tournament_andrey_nik(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        results = tournament.start()
        self.assertTrue(results[max(results)] == "Ник")

    @frozen_test
    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        results = tournament.start()
        self.assertTrue(results[max(results)] == "Ник")


if __name__ == '__main__':
    unittest.main()
