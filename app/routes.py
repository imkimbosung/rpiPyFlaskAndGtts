# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask, render_template,jsonify,json
from mGTTs import mGTTs

app = Flask(__name__)      
 
m = mGTTs()
@app.route('/')
def home():
  # m.run('테스트')
  return render_template('home.html')

@app.route('/summary')
def summary():
    # data = make_summary()
    m.run('테스트')
    response = app.response_class(
        response=json.dumps({'success' : True}),
        status=200,
        mimetype='application/json'
    )
    return response
 

if __name__ == '__main__':
  app.run(debug=True)
