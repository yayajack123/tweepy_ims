import pymysql

db = pymysql.connect("localhost", "root", "", "db_tweepy")
cursor_db = db.cursor()
