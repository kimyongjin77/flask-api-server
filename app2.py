from flask import Flask, jsonify
from http import HTTPStatus

app=Flask(__name__)

@app.route('/hithere', methods=['GET'])
def hi_there():
    return 'Hi there~~'

@app.route('/add', methods=['GET'])
def add():
    data=123 + 345
    return str(data)

@app.route('/', methods=['GET'])
def roof():
    return '안녕하세요'

@app.route('/act/data', methods=['GET'])
def act():
    ret={
            'cont':2,
            'students':[
                            {'name':'홍길동', 'age':20},
                            {'name':'홍길동', 'age':25}
                        ]
        }
    return jsonify(ret)

if __name__=='__main__':
    app.run()