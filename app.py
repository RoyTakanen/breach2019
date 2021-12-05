from flask import Flask, render_template, redirect
from os import environ

import requests
import time

app = Flask(__name__)

print("Ladataan suomen tietovuotoa...")
if environ.get("DL_URL"):
   finland = requests.get(environ.get("DL_URL")).content.splitlines()
else:
   finland = open("data/Finland.txt", "r").read().splitlines()
print("Suomen tietovuoto ladattu!")

def search(wanted_phone):
   for index, line in enumerate(finland):
      phone = line.split(":")[0]
      if phone == wanted_phone:
         return index

@app.route('/')
def etusivu():
   return render_template('etusivu.html')

@app.route('/info/<phone>')
def get_info(phone):
   start_time = time.time()
   try:
      index = search(phone)

      splittedline = finland[index].split(":")

      user = {
         "fb": splittedline[1],
         "first_name": splittedline[2],
         "las_name": splittedline[3],
         "gender": splittedline[4],
         "homeplace": splittedline[5],
         "birthplace": splittedline[6],
         "other2": splittedline[7],
         "other3": splittedline[8],
         "other4": splittedline[9],
         "other5": splittedline[10],
         "other6": splittedline[11]
      }

      finish_time = '{:f}'.format(time.time() - start_time)

      return render_template('info.html', info=user, time=finish_time)
   except:
      finish_time = '{:f}'.format(time.time() - start_time) 
      return render_template('nope.html', time=finish_time)

@app.route('/*')
def not_found():
   return redirect("/")


if __name__ == '__main__':
   app.run(debug = True)
