from flask import Flask, request
from flask_restful import Resource, Api
import os
import mysql.connector

app = Flask(__name__)


@app.route("/hydrate")
def read_db_values():
	user_value = {}
	config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'dashboard_info'
    }

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute("SELECT to_addr,subject,from_addr,password,dd_public_dashboard_url FROM `emailer_info` LIMIT 1");
	records = cursor.fetchall()

	for row in records: 
		to_addr = row[0]
		subject = row[1]
		from_addr = row[2]
		password = row[3]
		dd_public_dashboard_url = row[4]

		user_value = {
			"to_addr" : to_addr,
			"subject" : subject,
			"from_addr" : from_addr,
			"password" : password,
			"dd_public_dashboard_url" : dd_public_dashboard_url
		}

	print("$$$$$$")
	print(user_value['dd_public_dashboard_url'])
	print("$$$$$$")

	gen_image = "/usr/bin/xvfb-run -a /usr/bin/wkhtmltoimage --javascript-delay 20000 '{}' test.png".format(user_value['dd_public_dashboard_url'])
	print(gen_image)
	os.system(gen_image)

	return {'data': 'Screenshot taken.'}, 200

	cursor.close()
	connection.close()

if __name__ == '__main__':
    app.run()
