import unittest
from entity.result import Result
from repository.result_repository import result_repository


class TestResultRepository(unittest.TestCase):
    def setUp(self) -> None:
        result_repository.delete_all()
        self.result_test1 = Result("Test1", "9, 9, 10", 100, 50)
        self.result_test2 = Result("Test2", "16, 16, 30", 300, 90)

    def test_create(self):
        result_repository.create(self.result_test1)
        results = result_repository.find_all()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].username, self.result_test1.username)
        self.assertEqual(results[0].level, self.result_test1.level)
        self.assertEqual(results[0].time, self.result_test1.time)
        self.assertEqual(results[0].moves, self.result_test1.moves)

    def test_find_all(self):
        result_repository.create(self.result_test1)
        result_repository.create(self.result_test2)
        results = result_repository.find_all()

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0].username, self.result_test1.username)
        self.assertEqual(results[0].level, self.result_test1.level)
        self.assertEqual(results[0].time, self.result_test1.time)
        self.assertEqual(results[0].moves, self.result_test1.moves)

        self.assertEqual(results[1].username, self.result_test2.username)
        self.assertEqual(results[1].level, self.result_test2.level)
        self.assertEqual(results[1].time, self.result_test2.time)
        self.assertEqual(results[1].moves, self.result_test2.moves)
