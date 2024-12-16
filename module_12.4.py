import logging
import unittest

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)

from HumanMoveTest.runner import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner(name="TestRunner")
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except Exception as e:
            logging.warning(f"Ошибка: {e}")

    def test_run(self):
        try:
            runner = Runner(name=12345)  # Здесь будет выброшено исключение
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

if __name__ == '__main__':
    unittest.main()
