from flask import Flask
from flask import request
from flask import jsonify
from collections import defaultdict
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(database="pet-hotel", host = "localhost", port = "5432")

from collections import namedtuple

# def create_record(obj, fields):
#     ''' given obj from db returns named tuple with fields mapped to values '''
#     Record = namedtuple("Record", fields)
#     mappings = dict(zip(fields, obj))
#     return Record(**mappings)

def make_dictionary(row, columns):
  newDict = {}
  for index in range(len(row)):
    # print(columns[index], ' ', row[index])
    key = columns[index]
    value = row[index]
    newDict[key] = value
  return newDict
    





@app.route('/api/history',  methods=['GET', 'POST', 'PUT'])
def getHistory():

  cur = conn.cursor()
  cur.execute('SELECT * FROM "history"')

  rows = cur.fetchall()
  columns = [desc[0] for desc in cur.description]
  arrayOfHistory = []
  for row in rows:
    arrayOfHistory.append(make_dictionary(row, columns))

  cur.close()
  
  return jsonify(arrayOfHistory)


@app.route('/api/owners',  methods=['GET', 'POST', 'PUT', 'DELETE'])
def getOwners():

  cur = conn.cursor()
  cur.execute('SELECT * FROM "owners"')

  rows = cur.fetchall()
  columns = [desc[0] for desc in cur.description]
  arrayOfOwners = []
  for row in rows:
    arrayOfOwners.append(make_dictionary(row, columns))

  cur.close()
  return jsonify(arrayOfOwners)


