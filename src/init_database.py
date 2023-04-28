from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS results")
    connection.commit()


def create_table(connection):

    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE results (
            id INTEGER PRIMARY KEY,
            username TEXT,
            level TEXT,
            time INTEGER,
            moves INTEGER
            )
        """)
    connection.commit()


def init_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_table(connection)


if __name__ == "__main__":
    init_database()
