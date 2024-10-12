[![CI](https://github.com/nogibjj/Cindy_Gao_Week6_Mini_Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Cindy_Gao_Week6_Mini_Project/actions/workflows/cicd.yml)
# Complex SQL Query for a MySQL Database
## Requirements:

* Design a complex SQL query involving joins, aggregation, and sorting
* Provide an explanation for what the query is doing and the expected results

## Project Structure:

- **.devcontainer**: Sets up a consistent development environment across different machines.
- **.github/workflows**: Defines automated workflows for CI/CD tasks with 3 Repository secrets: DATABRICKS_API_KEY, SQL_HTTP and SQL_SERVER_HOST.
- **Makefile**: Manages tasks like installing dependencies, formatting code, linting, and testing.
- **requirements**: Lists the Python packages including the databrick packages required by the project.
- **main.py**: Contains the main code and functions for `query.py`.
- **test_main.py**: Contains test cases for `mylib`.
- **README.md**: Provides documentation and information for the project.
- **data**: Contains extracted dataset CSV file: `murder_2015_final.csv`.
- **mylib**: Contains:
  - `extract.py`: Extracts a dataset from a URL.
  - `query.py`: Contains a function called query including query with creating and joining a temporary table called **temp_murders**. I've included a more detailed explanation below.
  - `transform_load.py`: Establishing a database connection called **jg626_murdersdb** to Databricks.

```plaintext
Cindy_Gao_sqlite_lab/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── data/
│   └── murder_2015_final.csv
├── main.py
├── mylib/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── query_log.md
├── requirements.txt
├── setup.sh
└── test_main.py
```


## Raw Data:
https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/murder_2016/murder_2015_final.csv <br><br>
The original dataset presents the numbers of murders in 2014 and 2015, grouped by different cities in the US. <br><br>
Here is a screenshot of the database connection on Databricks: <br><br>
![image](https://github.com/user-attachments/assets/dc62ee8b-1a1c-4219-9577-257252ea9ac5)
![image](https://github.com/user-attachments/assets/6948895e-a7bd-4a7c-8558-b473abee94e6)

## SQL Query Explanation:
The query joins the original table **jg626_murdersdb** with a temporary table **temp_murders**, calculates the average number of murders for each state in 2014 and 2015 and then combines these averages with the actual number of murders in each city. It then orders the results by state and city. <br><br>
Here is a screenshot of SQL editor on Databricks for the complex query: <br><br>
```Python
WITH temp_murders AS (SELECT state,
                    AVG(2015_murders) AS avg_state_2015_murders,
                    AVG(2014_murders) AS avg_state_2014_murders
                FROM jg626_murdersDB
                GROUP BY state)
SELECT city,jg626_murdersDB.state, 2015_murders,avg_state_2015_murders,2014_murders,avg_state_2014_murders
FROM jg626_murdersDB
JOIN temp_murders
ON jg626_murdersDB.state = temp_murders.state
ORDER BY jg626_murdersDB.state,city
```
<br><br>
And a screenshot for the data output:<br><br>
![image](https://github.com/user-attachments/assets/ffa241ef-3ac5-450d-850d-71210ecc2411)






