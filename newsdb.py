#!/usr/bin/env python2
# "Database code" for the DB news.
import psycopg2

DBNAME = "news"


# question 1
def get_most_popular_three_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("\
        SELECT title, count(*) AS num\
        FROM articles JOIN article_title\
        ON articles.slug = article_title.replace\
        GROUP BY title\
        ORDER BY num DESC\
        LIMIT 3")
    result = c.fetchall()
    print 'What are the most popular three articles of all time?'
    for article in result:
        print '%s - %s views' % (article[0], article[1])
    db.close()


# question 2
def get_most_famous_author():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("\
        SELECT name, count(*) AS num\
        FROM articles JOIN article_title\
        ON articles.slug = article_title.replace\
        JOIN authors\
        ON articles.author = authors.id\
        GROUP BY articles.author, name\
        ORDER BY num DESC\
        LIMIT 1")
    result = c.fetchone()
    print ' Who are the most popular article authors of all time?'
    print '%s - %s views' % (result[0], result[1])
    db.close()


# question 3
def error_day():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("\
        SELECT date(time),\
        (SUM( CASE WHEN status LIKE '404%' THEN 1 ELSE 0 END ) * 1.0 /\
        COUNT(status)) AS ratio\
        FROM log\
        GROUP BY date(time)\
        HAVING (SUM( CASE WHEN status LIKE '404%' THEN 1 ELSE 0 END ) * 1.0 /\
        COUNT(status)) >= 0.01")
    result = c.fetchall()
    print 'On which days did more than 1% of requests lead to errors?'
    for item in result:
        print '%s - %s errors' % (item[0], "{:.2%}".format(item[1]))
    db.close()

get_most_popular_three_articles()
get_most_famous_author()
error_day()
