import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __eq__(self, other):
        return self.name == other.name

    def run(self, distance):
        return distance / self.speed

    def walk(self, distance):
        return distance / (self.speed / 2)


class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants

    def start(self):
        results = {}
        for runner in self.participants:
            time = runner.run(self.distance)
            results[time] = runner.name
        return dict(sorted(results.items()))


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(f"{key}: {cls.all_results[key]}")

    def test_tournament_usain_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner3])
        self.all_results = tournament.start()
        print(self.all_results)  # Добавляем вывод результатов на консоль
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    def test_tournament_andrey_nik(self):
        tournament = Tournament(90, [self.runner2, self.runner3])
        self.all_results = tournament.start()
        print(self.all_results)  # Добавляем вывод результатов на консоль
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")

    def test_tournament_usain_andrey_nik(self):
        tournament = Tournament(90, [self.runner1, self.runner2, self.runner3])
        self.all_results = tournament.start()
        print(self.all_results)  # Добавляем вывод результатов на консоль
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")


if __name__ == "__main__":
    unittest.main()
