"""Log Analysis program"""

import psycopg2


def getAnswer1():
  """Retrieves the top 3 most popular articles from the database."""
  db = psycopg2.connect("dbname=news")
  cur = db.cursor()
  print('Please wait...\n')
  cur.execute("""select articles.title, count(log.path) as views
                 from articles join log
                 on articles.slug = right(log.path, length(articles.slug))
                 group by articles.title
                 order by views desc
                 limit 3;""")
  results = cur.fetchall()
  db.close()
  return results


if __name__ == '__main__':
  """Answer question 1: What are the most popular three articles of all time? Which articles have been accessed the most?"""
  articles = getAnswer1()
  print ("The three most popular articles of all time are:\n")
  for article in articles:
    print('  "{}" - {} views').format(article[0], article[1])

  """Answer question 2: Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?"""
  #mostPopularAuthors = getAnswer2()


  """Answer question 3: On which days did more than 1% of requests lead to errors?"""
  #errorDay = getAnswer3()
