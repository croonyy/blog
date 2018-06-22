# encoding:utf-8
# !flask/bin/python
from app import app

app.run(debug=True,
        host='172.20.16.86',
        port='80'
        )
