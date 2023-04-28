import unittest
from service.result_service import ResultService


class FakeResultRepository:
    def __init__(self):
        self.results = []

    def find_all(self):
        return self.results

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
