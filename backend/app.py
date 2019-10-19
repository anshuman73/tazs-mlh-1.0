from flask import Flask, request


app = Flask(__name__)


if '__main__' == __name__:
    app.run(host='0.0.0.0', port=8000, debug=False)