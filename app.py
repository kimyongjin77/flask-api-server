from flask import Flask

app=Flask(__name__)

# api가 있어야 한다. 해당 경로로 GET요청이 오면 함수를 실행하여 응답하라..
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'

if __name__=='__main__':
    app.run()