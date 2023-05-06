from database_connection import get_database_connection
from entity.result import Result


def get_stat_by_row(row):
    return Result(row["username"], row["level"], row["time"], row["moves"]) if row else None


class ResultRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM results")
        results = cursor.fetchall()
        return list(map(get_stat_by_row, results))
    
    def find_ten_best(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM results ORDER BY time LIMIT 10")
        results = cursor.fetchall()
        return list(map(get_stat_by_row, results))

    def create(self, result):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO results(username, level, time, moves) VALUES (?,?,?,?)",
                       (result.username, result.level, result.time, result.moves))
        self._connection.commit()
        return result

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM results")
        self._connection.commit()


result_repository = ResultRepository(get_database_connection())
