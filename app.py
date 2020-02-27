from flask import Flask
from flask import request
from flask import jsonify
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(database="pet-hotel", host = "localhost", port = "5432")


@app.route('/api/history',  methods=['GET', 'POST', 'PUT'])
def hello_world():

  cur = conn.cursor()
  cur.execute('SELECT * FROM "history"')
  rows = cur.fetchall()

  print(rows)
  print([desc[0] for desc in cur.description])
  # print(cur.description)
  cur.close()
  return jsonify(rows)


