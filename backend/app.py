from flask import Flask, request
from flask_restful import Resource, Api
import test

app = Flask(__name__)
api = Api(app)


class testclass(Resource):
	def get(self, first_number,second_number):
		return {'data': test.run_test(first_number,second_number)}

api.add_resource(testclass, '/test/<first_number>/<second_number>')

if __name__ == '__main__':
    app.run()
