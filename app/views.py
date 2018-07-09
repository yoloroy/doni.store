from app import app
import pymysql
from random import randint
from json import dumps


@app.route('/')
@app.route('/index')
def index():
    return "He110!"

@app.route('/randitem')
def randitem():
    db = pymysql.connect("localhost", "gifts", "fNp65A7pk", "gifts")
    #db = pymysql.connect("localhost", "root", "gfhjkm", "doni")
    cursor = db.cursor()
    cursor.execute("use gifts")
    #cursor.execute("use doni")
    cursor.execute("select * from gifts")
    db = cursor.fetchall()
    db = db[randint(0, len(db) - 1)]
    db = {'name': db[1],
          'img': db[2],
          'url': db[3],
          'price': db[4]}
    return dumps(db)
