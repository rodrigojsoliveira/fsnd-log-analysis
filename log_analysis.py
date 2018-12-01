"""Log Analysis program"""

import psycopg2


if __name__ == '__main__':
  """Answer question 1: What are the most popular three articles of all time? Which articles have been accessed the most?"""
  mostPopularArticles = getAnswer1()


  """Answer question 2: Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?"""
  mostPopularAuthors = getAnswer2()


  """Answer question 3: On which days did more than 1% of requests lead to errors?"""
  errorDay = getAnswer3()
