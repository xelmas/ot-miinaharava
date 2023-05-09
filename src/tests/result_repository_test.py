import unittest
from entity.result import Result
from repository.result_repository import result_repository


class TestResultRepository(unittest.TestCase):
    def setUp(self) -> None:
        result_repository.delete_all()
        self.result_test1 = Result("Test1", "9, 9, 10", 100, 50)  # 4
        self.result_test2 = Result("Test2", "16, 16, 30", 300, 90)  # 9
        self.result_test3 = Result("Test3", "9, 9, 10", 400, 50)  # 10
        self.result_test4 = Result("Test4", "16, 16, 30", 50, 90)  # 3
        self.result_test5 = Result("Test5", "16, 16, 30", 212, 90)  # 7
        self.result_test6 = Result("Test6", "16, 16, 30", 212, 90)  # 8
        self.result_test7 = Result("Test7", "16, 16, 30", 501, 40)
        self.result_test8 = Result("Test8", "9, 9, 10", 40, 20)  # 2
        self.result_test9 = Result("Test9", "16, 16, 30", 150, 90)  # 6
        self.result_test10 = Result("Test10", "16, 16, 30", 120, 90)  # 5
        self.result_test11 = Result("Test11", "9, 9, 10", 20, 23)  # 1

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

    def test_find_top_ten(self):
        result_repository.create(self.result_test1)
        result_repository.create(self.result_test2)
        result_repository.create(self.result_test3)
        result_repository.create(self.result_test4)
        result_repository.create(self.result_test5)
        result_repository.create(self.result_test6)
        result_repository.create(self.result_test7)
        result_repository.create(self.result_test8)
        result_repository.create(self.result_test9)
        result_repository.create(self.result_test10)
        result_repository.create(self.result_test11)

        results = result_repository.find_top_ten()
        self.assertEqual(len(results), 10)

        self.assertEqual(results[0].time, self.result_test11.time)
        self.assertEqual(results[1].time, self.result_test8.time)
        self.assertEqual(results[2].time, self.result_test4.time)
        self.assertEqual(results[3].time, self.result_test1.time)
        self.assertEqual(results[4].time, self.result_test10.time)
        self.assertEqual(results[5].time, self.result_test9.time)
        self.assertEqual(results[6].time, self.result_test5.time)
        self.assertEqual(results[7].time, self.result_test6.time)
        self.assertEqual(results[8].time, self.result_test2.time)
        self.assertEqual(results[9].time, self.result_test3.time)
