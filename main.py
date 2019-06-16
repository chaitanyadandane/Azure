from flask import Flask, render_template, request
import sqlite3 as sql
import math
import time
from datetime import datetime, timedelta

app = Flask(__name__)

import csv 
import sys
import os

conn = sql.connect('db.db')

coloumn_names = ["time","latitude","longitude","depth","mag","magType","nst","gap","dmin","rms", "id", "place", "depthError", "magError", "magNst", "locationSource"]
myfile = open("quakes.csv","r")
csv_reader = csv.DictReader(myfile, fieldnames=coloumn_names)
next(csv_reader)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list', methods=['POST','GET'])
def list():
	if request.method == "POST":
		mag = request.form['mag']
		starttime = time.time()
		con = sql.connect("db.db")
		con.row_factory = sql.Row
		cur = con.cursor()

		cur.execute("select * from earthquakes where mag >"+ mag +"")

		rows = cur.fetchall();
		endtime = time.time()
		duration = endtime - starttime
		return render_template('list.html', ci=rows, time=duration)

if __name__ == '__main__':
  app.run(debug=True)
