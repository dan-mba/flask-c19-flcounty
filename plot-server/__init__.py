import os
from flask import Flask, jsonify, render_template
from .county import get_c19_data_county
from .graph import graph_county_df
from .countylist import COUNTIES

if "static-path" in os.environ:
  app = Flask(__name__, static_folder=os.environ['static-path']+'/static', template_folder=os.environ['static-path'])
  
else:
  app = Flask(__name__, static_folder='/usr/src/app/static', template_folder='/usr/src/app/template')


@app.route('/')
def home():
  return render_template("index.html")

@app.route('/api/<int:county_id>')
def county_api(county_id):
  df = get_c19_data_county(COUNTIES[county_id])
  if df is not None:
    data = graph_county_df(df)
    return jsonify(data)
  else:
    return jsonify({"count":"", "sum":""})
