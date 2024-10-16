"""
Tests of mylib goes here

"""

from mylib.extract import extract
from mylib.query import query
from databricks import sql
import os


def test_extract():
    extract_results = extract()
    assert extract_results is not None


def test_load():
    # Connect to Databricks
    server_h = os.getenv("SQL_SERVER_HOST")
    access_token = os.getenv("DATABRICKS_API_KEY")
    http_path = os.getenv("SQL_HTTP")

    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()

        table_name = "jg626_murdersDB"

        # Check to see if your first table is there
        c.execute(f"SHOW TABLES FROM default LIKE '{table_name}'")
        result1 = c.fetchall()

        # Check if there are rows in your first table
        c.execute(f"SELECT * FROM {table_name}")
        result2 = c.fetchall()

        c.close()

    # Confirm the first table is there and that there are rows inside
    assert result1 is not None
    assert len(result1) > 0

    assert result2 is not None
    assert len(result2) > 0


def test_query():
    query_results = query()
    assert query_results is not None


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
