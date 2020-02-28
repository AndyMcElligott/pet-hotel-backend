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


@app.route('/api/history',  methods=['GET', 'POST', 'PUT'])
def getHistory():

    arrayOfHistory = sqlSelect('SELECT * FROM "history"')
    return jsonify(arrayOfHistory)


@app.route('/api/owners',  methods=['GET', 'POST', 'PUT', 'DELETE'])
def getOwners():

    arrayOfOwners = sqlSelect('SELECT * FROM "owners"')
    return jsonify(arrayOfOwners)
