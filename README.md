# Logs Analysis

Reporting tool for analyzing the logs from a website database. This is a Udacity FS Nanodegree project.

## Prerequisites

- This application requires [Python 3.6](https://www.python.org/downloads/)
- The database used for this projects is [PostgreSQL 9.5.12](https://www.postgresql.org/download/)
- The application analyzes the `news` database, and it is assumed that the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) has been loaded.
- The reporting tool relies on 3 views, and those must be created before running it.

### Required Views 
The first view is used to modify the `path` column in the `log` table to match the `slug` column in the `articles` table.
Statement used to create the first view:
```
CREATE VIEW slug_log AS
    SELECT reverse(split_part(reverse(path), '/', 1)) "slug",
            status, time, id
    FROM log;
```
The second view is used to aggregate the number of errors for each day.
Statement used to create the second view:
```
CREATE VIEW errors AS
    SELECT to_char(time, 'Month DD, YYYY') AS date, count(*) AS num_of_err
    FROM log
    WHERE status LIKE '404%'
    GROUP BY date;
```
The third view is used to aggregate the number of requests for each day.
The statement used to create the third view:
```
CREATE VIEW requests AS
    SELECT to_char(time, 'Month DD, YYYY') AS date, count(*) AS num_of_req
    FROM log
    GROUP BY date;
```

## Running the Report
Run the report with `python3 LogsAnalysis.py`
The program connects to the database, executes one SQL query for each report, and then fetches the result.
The result is formatted into a legible form and it is printed out.