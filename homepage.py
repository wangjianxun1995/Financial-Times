from flask import Flask, jsonify
from flask import redirect
from flask import render_template
from flask import request
import re

from flask import url_for

app = Flask(__name__)


from flask import Flask
from flask import abort

app = Flask(__name__)

@app.errorhandler(404)
def internal_server_error(e):
    return '服务器搬家了'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)