from flask import Flask
from pyvinted import Vinted
from flask import request, jsonify


vinted = Vinted()
app = Flask(__name__)


@app.route("/search")
def search():
  query = request.args.get("query")
  items = vinted.items.search(query,900,1)
  
  return jsonify(len(items))