# encoding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


aaaaa


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# if __name__ == '__main__':
#    app.run()
