import json
from flask import Flask, request
from flask_restful import Resource, Api
from CalculationCl import MyMath
import numpy as np
# from calculation import Test
math=MyMath()

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class TestArray(Resource):
    def put(self):
        frq = np.array(json.loads(request.form['frecuencia']))
        db = np.array(json.loads(request.form['db']))
        val=math.interpolPkSemiFar(frq)
        return {'values': (val).tolist(), 'db': (db-val).tolist() }
    def get(self):
        frq=[]
        return { 'valores': frq }

class CompararPkSemi(Resource):
    def put(self):
        frq = np.array(json.loads(request.form['frecuencia']))
        db = np.array(json.loads(request.form['db']))
        val = math.interpolPkSemiFar(frq)
        return {'values': (val).tolist(), 'db': (db-val).tolist()}

api.add_resource(HelloWorld, '/hello')
api.add_resource(TestArray,'/test')
api.add_resource(CompararPkSemi, '/compararpksemi')

if __name__ == '__main__':
    app.run(debug=True)
