import unittest
from service.result_service import ResultService


class FakeResultRepository:
    def __init__(self):
        self.results = []

    def find_all(self):
        return self.results

    def find_top_ten(self):
        results = []
        ten_best = []
        for stat in self.results:
            results.append(stat.time)

        results.sort()
        for i in range(10):
            ten_best.append(results[i])
        return ten_best

    def create(self, result):
        self.results.append(result)
        return result

    def delete_all(self):
        self.results = []


class TestResultService(unittest.TestCase):
    def setUp(self):
        self.result_service = ResultService(FakeResultRepository())

    def test_create_result(self):
        self.result_service.create_result("Test", "9, 9, 10", 140, 20)
        results = self.result_service.get_results()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].username, "Test")
        self.assertEqual(results[0].level, "9, 9, 10")
        self.assertEqual(results[0].time, 140)
        self.assertEqual(results[0].moves, 20)

    def test_find_top_ten(self):
        self.result_service.create_result("Test1", "9, 9, 10", 20, 20)  # 2
        self.result_service.create_result("Tes2", "9, 9, 10", 100, 20)  # 6
        self.result_service.create_result("Test3", "9, 9, 10", 10, 20)  # 1
        self.result_service.create_result("Test4", "9, 9, 10", 90, 20)  # 4
        self.result_service.create_result("Test5", "9, 9, 10", 200, 20)  # 7
        self.result_service.create_result("Test6", "9, 9, 10", 300, 20)  # 9
        self.result_service.create_result("Test7", "9, 9, 10", 440, 20)  # 10
        self.result_service.create_result("Test8", "9, 9, 10", 200, 20)  # 8
        self.result_service.create_result("Test9", "9, 9, 10", 440, 20)
        self.result_service.create_result("Test10", "9, 9, 10", 30, 20)  # 3
        self.result_service.create_result("Test11", "9, 9, 10", 99, 20)  # 5
        self.result_service.create_result("Test12", "9, 9, 10", 520, 20)

        results = self.result_service.get_top_ten()
        self.assertEqual(len(results), 10)

        self.assertEqual(results[0], 10)
        self.assertEqual(results[1], 20)
        self.assertEqual(results[2], 30)
        self.assertEqual(results[3], 90)
        self.assertEqual(results[4], 99)
        self.assertEqual(results[5], 100)
        self.assertEqual(results[6], 200)
        self.assertEqual(results[7], 200)
        self.assertEqual(results[8], 300)
        self.assertEqual(results[9], 440)
