"""
Transforms and Loads data into the external databricks database
"""

from databricks import sql
import csv
import os
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into databricks
def load(dataset="data/murder_2015_final.csv"):
    """Transforms and Loads data into the local databricks database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)

    load_dotenv()
    server_h = os.getenv("sql_server_host")
    access_token = os.getenv("databricks_api_key")
    http_path = os.getenv("sql_http")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        # INSERT TAKES TOO LONG
        # c.execute("DROP TABLE IF EXISTS ServeTimesDB")
        c.execute("DROP TABLE IF EXISTS jg626_murdersDB")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS jg626_murdersDB (
                    city string,
                    state string,
                    2014_murders int,
                    2015_murders int,
                    change int
                )
            """
            )
        c.executemany("INSERT INTO jg626_murdersDB VALUES (?,?,?,?,?)", payload)
        c.close()
        return "success"


if __name__ == "__main__":
    load()
