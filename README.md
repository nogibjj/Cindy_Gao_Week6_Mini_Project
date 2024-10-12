# Complex SQL Query for a MySQL Database
## Requirements:

* Design a complex SQL query involving joins, aggregation, and sorting
* Provide an explanation for what the query is doing and the expected results

## Project Structure:

- **.devcontainer**: Sets up a consistent development environment across different machines.
- **.github/workflows**: Defines automated workflows for CI/CD tasks.
- **Makefile**: Manages tasks like installing dependencies, formatting code, linting, and testing.
- **requirements**: Lists the Python packages including the databrick packages required by the project.
- **main.py**: Contains the main code and functions for `query.py`.
- **test_main.py**: Contains test cases for `mylib`.
- **README.md**: Provides documentation and information for the project.
- **data**: Contains extracted dataset CSV file: `murder_2015_final.csv`.
- **mylib**: Contains:
  - `extract.py`: Extracts a dataset from a URL.
  - `query.py`: Contains functions including load query with joining a table using column: state, aggregating by group by the same state for different cities, and calculate the average murders for both 2014 and 2015, then sorting alphabetically by the state and city name.
  - `transform_load.py`: Establishing a database connection to Databrick.

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
The dataset presents the numbers of murders in 2014 and 2015, grouped by different cities in the US. <br><br>
Here is a screenshot of the database connection on Databricks: <br><br>
![image](https://github.com/user-attachments/assets/dc62ee8b-1a1c-4219-9577-257252ea9ac5)
![image](https://github.com/user-attachments/assets/6948895e-a7bd-4a7c-8558-b473abee94e6)


Here is a screenshot of SQL editor on Databricks for the complex query: <br><br>
![image](https://github.com/user-attachments/assets/204226e2-27d1-4e07-9d8a-e953f93ea74f)
And a screenshot for the data output:
![image](https://github.com/user-attachments/assets/ffa241ef-3ac5-450d-850d-71210ecc2411)






