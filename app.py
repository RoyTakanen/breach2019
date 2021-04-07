from flask import Flask, render_template, redirect, request
import pymongo 
import time

app = Flask(__name__)

dbclient = pymongo.MongoClient("mongodb://<user>:<password>@<hostname>:<port>/")

breach2019 = dbclient["breach2019"]
users = breach2019["users"]
visits = breach2019["stats"]

def add_visit(ip, page):
      visit = {
         "ip": ip,
         "page": page,
      }

      visits.insert_one(visit)


@app.route('/')
def etusivu():
   if request.headers.getlist("X-Forwarded-For"):
      ip = request.headers.getlist("X-Forwarded-For")[0]
      add_visit(ip, "Etusivu")

   return render_template('etusivu.html')

@app.route('/info/<phone>')
def get_info(phone):
   start_time = time.time()
   try:
      query = { "phone": phone }

      user = users.find(query)[0]
      finish_time = time.time() - start_time

      if request.headers.getlist("X-Forwarded-For"):
         ip = request.headers.getlist("X-Forwarded-For")[0]
         add_visit(ip, "Puhelin")

      return render_template('info.html', info=user, time=finish_time)
   except:
      finish_time = time.time() - start_time      
      return render_template('nope.html', time=finish_time)

@app.route('/*')
def not_found():
   if request.headers.getlist("X-Forwarded-For"):
      ip = request.headers.getlist("X-Forwarded-For")[0]
      add_visit(ip, "Ei löytynyt")
   return redirect("/")


if __name__ == '__main__':
   app.run(debug = True)
