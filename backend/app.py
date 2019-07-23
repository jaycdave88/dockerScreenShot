from flask import Flask, request
from flask_restful import Resource, Api
import order

app = Flask(__name__)
api = Api(app)

class control_flow(Resource):
	def get(self):
		return {'data': order.execute_commands()}, 200

api.add_resource(control_flow, '/execute')

if __name__ == '__main__':
    app.run()
