#!/usr/bin/env python3

"""
Log Analysis program.

This program will fetch data from
a database and answer three pre-defined questions.
The code was tested with Python v. 2.7 and will
run on version 3.0 and greater.

Written by Rodrigo Jose Sarmento Oliveira - Dec/2018
"""

import psycopg2


"""Define the 3 SQL queries used on the reporting application."""
top3articles = """select articles.title, count(log.path) as views
                  from articles join log
                  on '/article/' || articles.slug = log.path
                  group by articles.title
                  order by views desc
                  limit 3;"""

topAuthors = """select authors.name, sum(views_per_article.views) as total_views
                from authors join
                (select max(articles.author) as author_id,
                count(log.path) as views
                from articles join log
                on '/article/' || articles.slug = log.path
                group by articles.title) as views_per_article
                on authors.id = views_per_article.author_id
                group by authors.name
                order by total_views desc;"""

mostErrors = """select to_char(the_day, 'FMMonth DD, YYYY'), result from
                (select error_count.the_day,
                round((cast(errors as decimal)/total)*100,2) as result
                from
                (select date(time) as the_day, count(status) as total
                from log
                group by the_day) as logs_per_day
                join
                (select date(time) as the_day, count(status) as errors
                from log
                where status = '404 NOT FOUND'
                group by the_day) as error_count
                on logs_per_day.the_day = error_count.the_day
                order by error_count.the_day) as results
                where result > 1;"""


def getResults(selectQueryString):
    """Execute an SQL SELECT query and returns the retrieved data."""
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute(selectQueryString)
    results = cur.fetchall()
    db.close()
    return results


if __name__ == '__main__':
    """Answer question 1: What are the most popular three articles of all time?
       Which articles have been accessed the most?"""
    articles = getResults(top3articles)
    print ("\nThe three most popular articles of all time are:\n")
    for title, views in articles:
        print('  "{}" - {} views'.format(title, views))
    print('\n')

    """Answer question 2: Who are the most popular article authors of all time?
       That is, when you sum up all of the articles each author has written,
       which authors get the most page views?"""
    authors = getResults(topAuthors)
    print ("The most popular article authors are:\n")
    for author in authors:
        print('  {} - {} views'.format(author[0], author[1]))
    print('\n')

    """Answer question 3: On which days did more than 1% of
       requests lead to errors?"""
    errorDays = getResults(mostErrors)
    print ("More than 1% of requests lead to errors on this day:\n")
    for errorDay in errorDays:
        print('  {} - {}% errors'.format(errorDay[0], errorDay[1]))
    print('\n')
