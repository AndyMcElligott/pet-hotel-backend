from flask import Flask
from flask import request
from flask import jsonify
from collections import defaultdict
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(database="pet-hotel", host="localhost", port="5432")

# def make_dictionary(row, columns):
#   newDict = {}
#   for index in range(len(row)):
#     # print(columns[index], ' ', row[index])
#     key = columns[index]
#     value = row[index]
#     newDict[key] = value
#   return newDict


def make_dictionary(columns, row):
    rowWithKeys = dict(zip(columns, row))
    return rowWithKeys


def sqlSelect(query):
    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    rowsWithKeys = []
    for row in rows:
        rowsWithKeys.append(make_dictionary(columns, row))

    cur.close()
    return rowsWithKeys


def sqlInsert(queryText, values):
    cur = conn.cursor()
    cur.execute(queryText, values)
    conn.commit()
    cur.close()


@app.route('/api/history',  methods=['GET', 'POST'])
def getHistory():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        queryText = """INSERT INTO "history" ("owner", "pet", "breed", "color", "checked_in")
                    VALUES (%s, %s, %s, %s, TRUE)"""
        sqlInsert(queryText, (data['owner'], data['name'], data['breed'], data['color']))
        return 'worked'

    elif request.method == 'GET':
        arrayOfHistory = sqlSelect('SELECT * FROM "history"')
        return jsonify(arrayOfHistory)


@app.route('/api/owners',  methods=['GET', 'POST'])
def getOwners():
    if request.method == 'POST':
      data = request.get_json()
      queryText = """INSERT INTO "owners" ("name")
                    VALUES (%s)"""
      sqlInsert(queryText, (data['name'], ))
      return 'Hi'

    elif request.method == 'GET':
      arrayOfOwners = sqlSelect('SELECT * FROM "owners"')
      return jsonify(arrayOfOwners)
