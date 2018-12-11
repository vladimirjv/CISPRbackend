import json
import sys
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from CalculationCl import MyMath
import numpy as np
# from calculation import Test
math=MyMath()

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('lista')
parser.add_argument('db')
parser.add_argument('type')


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
        val = math.interpolPkSemiFar(frq)
        return {'values': (val).tolist(), 'db': (db-val).tolist()}
        # return {'values': (frq).tolist(), 'db': (db).tolist()}
    def get(self):
        frq=[]
        return { 'valores': frq }

class CompararPkSemi(Resource):
    support_cors = True
    cors_origin = '*'
    cors_headers = 'origin, content-type, x-request-with'
    def put(self):
        args = parser.parse_args()
        frq = args['lista']
        db = args['db']
        typeQuery = args['type']
        frq = list(map(float, frq.split(",")))
        pk = list(map(float, db.split(",")))
        frqA=np.array(frq)
        pkA=np.array(pk)
        val= []
        if typeQuery=="SF":
            val=math.interpolPkSemiFar(frqA)
        if typeQuery =="SM":
            val = math.interpolPkSemiMiddle(frqA)
        if typeQuery == "SC":
            val = math.interpolPkSemiClose(frqA)
        # val=np.around(val)
        diff=np.around((pkA-val),2)
        mape = np.around((np.mean(np.abs((val - pkA) / val)) * 100),2)
        val=np.around(val,2)
        return {'frecuencia': frq, 'pk': pk, 'realPk': (val).tolist(),'diff':(diff).tolist(),'mape':mape, 'type':typeQuery}
    def get(self):
        frq=self.frq
        pk=self.pk
        return {'frecuencia': frq, 'pk':pk, 'realPk': ''}

class DatosSemiFar(Resource):
    def get(self):
        frq=np.around(math.xp270)
        pk = math.interpolPkSemiFar(frq)
        qp = np.around(math.interpolQpSemiFar(frq),2)
        avg = np.around(math.interpolAvgSemiFar(frq),2)
        return {'frecuencia':(frq).tolist(),'pk':(pk).tolist(),'qp':(qp).tolist(),'avg':(avg).tolist()}

api.add_resource(HelloWorld, '/hello')
api.add_resource(TestArray,'/test')
api.add_resource(CompararPkSemi, '/compararpksemi')
api.add_resource(DatosSemiFar, '/datasf')

if __name__ == '__main__':
    app.run(debug=True)
