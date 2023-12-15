# アプリケーション bottleフレームワークの使い方
# pip install bottle
from bottle import route, run

@route('/')
def index():
    return 'Hello, world!'

run(host='localhost', port=8080, debug=True)