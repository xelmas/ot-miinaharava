from database_connection import get_database_connection
from entity.result import Result


def get_stat_by_row(row):
    return Result(row["username"], row["level"], row["time"], row["moves"]) if row else None


class ResultRepository:
    """Handles saving and retrieving of the game results in a database."""

    def __init__(self, connection) -> None:
        """Initializes a new ResultRepository object with database connection.

        Args:
            connection: The database connection.
        """
        self._connection = connection

    def find_all(self):
        """Retrieves all the results from the database.

        Returns:
            A list of all the result objects.
        """

        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM results")
        results = cursor.fetchall()
        return list(map(get_stat_by_row, results))

    def find_top_ten(self):
        """Retrieves the top ten results from the database.

        Returns:
            A list of the top ten result objects.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM results ORDER BY time LIMIT 10")
        results = cursor.fetchall()
        return list(map(get_stat_by_row, results))

    def create(self, result):
        """Creates a new result in the database.

        Args:
            result (Result): The result object to create.

        Returns:
            The created result object.
        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO results(username, level, time, moves) VALUES (?,?,?,?)",
                       (result.username, result.level, result.time, result.moves))
        self._connection.commit()
        return result

    def delete_all(self):
        """Deletes all the results from the database."""

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM results")
        self._connection.commit()


result_repository = ResultRepository(get_database_connection())
