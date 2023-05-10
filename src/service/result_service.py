from entity.result import Result
from repository.result_repository import (result_repository as defaul_repo)


class ResultService:
    """Handles application logic for creating and retrieving game results.

    It uses results repository to store and retrieve the results.
    """

    def __init__(self, result_repository=defaul_repo) -> None:
        """_summary_

        Args:
            result_repository (ResultRepository, optional): The repository for storing 
                and retrieving results. Defaults to defaul_repo.
        """
        self._result = None
        self._result_repository = result_repository

    def create_result(self, username, level, time, moves):
        """Creates a new result and saves it in the result repository.

        Args:
            username (str): The player's name.
            level (_type_): The level played.
            time (_type_): The time passed from the start.
            moves (_type_): The number of moves made during the game.

        Returns:
            The created result object.
        """
        result = Result(username, level, time, moves)
        return self._result_repository.create(result)

    def get_results(self):
        """Retrieves all the results from the result repository.

        Returns:
            A list of all the result objects.
        """
        return self._result_repository.find_all()

    def get_top_ten(self):
        """Retrieves the top ten results from the result repository.

        Returns:
            A list of top ten result objects.
        """
        return self._result_repository.find_top_ten()


result_service = ResultService()
