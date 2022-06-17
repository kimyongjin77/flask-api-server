from unittest import result
from flask import Flask, jsonify, request

app=Flask(__name__)

#클라이언트 두개의 숫자를 받아서 계산하여 리턴
@app.route('/add_two_nums', methods=['POST'])
def add():
    #클라이언트로부터 두 수를 받는다.
    #요청 POST http://127.0.0.1:5000/add_two_nums
    #body={"x":30, "y":40}
    data=request.get_json()
    ret=data['x']+data['y']
    #응답 {"result":70}
    result={"result":ret}
    return jsonify(result)

if __name__=='__main__':
    app.run(port=5000)