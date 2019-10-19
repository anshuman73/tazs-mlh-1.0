from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

if '__main__' == __name__:
    app.run(host='0.0.0.0', port=8000, debug=False)