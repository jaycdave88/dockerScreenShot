from flask import Flask, request
import os
import mysql.connector
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

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

	try:
		gen_image = "/usr/bin/xvfb-run -a /usr/local/bin/wkhtmltoimage '{}' payload.png".format(user_value['dd_public_dashboard_url'])

		os.system(gen_image)

		fromaddr = user_value['from_addr']
		toaddr = user_value['to_addr']

		# instance of MIMEMultipart 
		msg = MIMEMultipart() 
  
		# storing the senders email address   
		msg['From'] = user_value['from_addr'] 
		  
		# storing the receivers email address  
		msg['To'] = user_value['to_addr']
		  
		# storing the subject  
		msg['Subject'] = user_value['subject']
		print("$$$$")
		print(msg['To'])
		print("$$$$")

		# string to store the body of the mail 
		body = "Here is the Screenshot!"
		  
		# attach the body with the msg instance 
		msg.attach(MIMEText(body, 'plain')) 
		  
		# open the file to be sent  
		filename = "payload.png"
		attachment = open("/app/payload.png", "rb") 
		  
		# instance of MIMEBase and named as p 
		p = MIMEBase('application', 'octet-stream') 
		  
		# To change the payload into encoded form 
		p.set_payload((attachment).read()) 
		  
		# encode into base64 
		encoders.encode_base64(p) 
		   
		p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
		  
		# attach the instance 'p' to instance 'msg' 
		msg.attach(p) 
		  
		# creates SMTP session 
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		  
		# start TLS for security 
		s.starttls() 
		  
		# Authentication 
		s.login(fromaddr, user_value["password"]) 
		  
		# Converts the Multipart msg into a string 
		text = msg.as_string() 
		  
		# sending the mail 
		s.sendmail(fromaddr, toaddr, text) 
		  
		# terminating the session 
		s.quit() 


		return {'data': 'Screenshot taken.'}, 200

	except Exception as e:
		raise e

	cursor.close()
	connection.close()

if __name__ == '__main__':
    app.run()
