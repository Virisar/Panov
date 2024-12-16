import unittest
from HumanMoveTest.module_12_3 import RunnerTest, TournamentTest

# Создание объекта TestSuite
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
