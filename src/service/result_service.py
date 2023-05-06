from entity.result import Result
from repository.result_repository import (result_repository as defaul_repo)


class ResultService:
    def __init__(self, result_repository=defaul_repo) -> None:
        self._result = None
        self._result_repository = result_repository

    def create_result(self, username, level, time, moves):
        result = Result(username, level, time, moves)
        return self._result_repository.create(result)

    def get_results(self):
        return self._result_repository.find_all()
    
    def get_ten_best(self):
        return self._result_repository.find_ten_best()


result_service = ResultService()
