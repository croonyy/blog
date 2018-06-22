# encoding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# views模块导入为什么放这里而不放头部，
# 因为app包里面的view模块引用了app变量，如果放头部则app = Flask(__name__)都没有实例化就引用app变量，
# 所以一定要在app = Flask(__name__)实例化了之后才能引用views模块
from app import views

# if __name__ == '__main__':
#    app.run()
