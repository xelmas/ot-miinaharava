from database_connection import get_database_connection


def drop_table(connection):
    """Drops the table "results" from the database if it already exists."""

    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS results")
    connection.commit()


def create_table(connection):
    """Creates the "results" table in the database."""

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
    """Initializes the database by dropping and creating the "results" table."""

    connection = get_database_connection()

    drop_table(connection)
    create_table(connection)


if __name__ == "__main__":
    init_database()
