"""Query the database"""

import os
import csv
from databricks import sql
from dotenv import load_dotenv


def query(dataset="data/murder_2015_final.csv"):
    """A complex SQL query involving joins, aggregation, and sorting"""
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
        c.execute(
            """
                WITH temp_murders AS (SELECT state,
                    AVG(2015_murders) AS avg_state_2015_murders,
                    AVG(2014_murders) AS avg_state_2014_murders
                FROM jg626_murdersDB
                GROUP BY state)
                SELECT city,jg626_murdersDB.state, 2015_murders,avg_state_2015_murders,2014_murders,avg_state_2014_murders
                FROM jg626_murdersDB
                JOIN temp_murders
                ON jg626_murdersDB.state = temp_murders.state
                ORDER BY jg626_murdersDB.state ASC,city ASC
                """
        )
        result = c.fetchall()
        print(result)
        c.close()
