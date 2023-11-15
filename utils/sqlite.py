import sqlite3


def create_gpt_result_db():
    # Connect to the SQLite database (creates a new one if it doesn't exist)
    conn = sqlite3.connect("gpt_result.db")

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create a table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS gpt_result (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """
    )

    # Insert data into the table
    cursor.execute(
        """
        INSERT INTO gpt_result (name, content) VALUES (?, ?)
    """,
        ("gpt_result", "null"),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return True


def save_gpt_result(result: str):
    # Connect to the SQLite database (creates a new one if it doesn't exist)
    conn = sqlite3.connect("gpt_result.db")
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE gpt_result
        SET content = ?
        WHERE name = ?
    """,
        (result, "gpt_result"),
    )
    conn.commit()
    cursor.close()
    conn.close()
    return True


def fetch_gpt_result():
    # Connect to the SQLite database (creates a new one if it doesn't exist)
    conn = sqlite3.connect("gpt_result.db")
    # Create a cursor object to interact with the database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gpt_result")
    rows = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    for row in rows:
        return row[2]
    return None


# save_gpt_result("sdf")
# print(fetch_gpt_result())
