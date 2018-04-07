#!/usr/bin/env python3

"""LogsAnalysis.py: Reporting tool for analyzing logs from a newspaper site."""

import psycopg2

__author__ = "Ivan Zlatev"
__copyright__ = "Copyright 2018, Udacity FS Nanodegree Project"
__license__ = "MIT"


def analyze_logs():
    """Connect to DB, execute queries, and print the report."""
    db = psycopg2.connect(database="news")
    c = db.cursor()

    print('\nThe most popular three articles of all time are:')
    c.execute('SELECT title, count(*) AS views '
              'FROM articles, slug_log '
              'WHERE articles.slug = slug_log.slug '
              'GROUP BY title '
              'ORDER BY views DESC fetch first 3 rows only ')
    result1 = c.fetchall()
    for item in result1:
        print('"%s"' % item[0], '-', item[1], 'views')

    print('\nThe most popular authors of all time are:')
    c.execute('SELECT name, count(*) AS views '
              'FROM authors, articles, slug_log '
              'WHERE authors.id = articles.author '
              'AND articles.slug = slug_log.slug '
              'GROUP BY name '
              'ORDER BY views DESC ')
    result2 = c.fetchall()
    for item in result2:
        print(item[0], '-', item[1], 'views')

    print('\nDays on which more than 1% of requests led to errors:')
    c.execute("SELECT errors.date, "
              "to_char((num_of_err / num_of_req::float) * 100.0, '999D99%') "
              "AS percent_err "
              "FROM errors JOIN requests ON errors.date = requests.date "
              "WHERE (num_of_err / num_of_req::float) >= 0.01 ")
    result3 = c.fetchall()
    db.close()
    for item in result3:
        print(item[0], '-', item[1], 'errors')


analyze_logs()
