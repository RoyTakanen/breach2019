from flask import Flask, render_template, redirect
import time

app = Flask(__name__)


@app.route('/')
def etusivu():
   return render_template('etusivu.html')

@app.route('/info/<phone>')
def get_info(phone):
   start_time = time.time()
   try:
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
