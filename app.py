from flask import Flask, request
from flask_restful import Resource, Api
import json
from calculation import EvaluarBS

app = Flask(__name__)
api = Api(app)

lista=[]

@app.route('/')
def hello_world():
    return 'Hello, World!'

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class TestArray(Resource):
    def put(self):
        data=request.form['list']
        lista=json.loads(data)
        #with requests from python
        # put('http://127.0.0.1:5000/test', data={'list': '[23,23,1243]'}).json()
        return { 'valores':lista }

class Compensar(Resource):
    def put(self):
        frq=json.loads(request.form['frecuencia'])
        # pk=json.loads(request.form['pk'])
        compensacion=EvaluarBS(frq)
        return {'compensacion' : compensacion }


api.add_resource(HelloWorld, '/hello')
api.add_resource(TestArray,'/test')
# api.add_resource(Compensar, '/compensacion')

if __name__ == '__main__':
    app.run(debug=True)
