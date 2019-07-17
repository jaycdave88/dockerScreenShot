from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from typing import List, Dict
import mysql.connector

DEBUG = True
app = Flask(__name__, template_folder="./flask/templates/")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

class ReusableForm(Form):
    to_addr = TextField('To:')
    subject = TextField('Subject:')
    from_addr = TextField('From:')
    password = TextField('Password:')
    dd_public_dashboard_url = TextField('Public Dashboard URL:')

def write_to_db(to_addr,subject,from_addr,password,dd_public_dashboard_url) -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'dashboard_info'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO `emailer_info` (to_addr, subject, from_addr, password, dd_public_dashboard_url) VALUES (%s,%s,%s,%s,%s)", (to_addr, subject, from_addr, password, dd_public_dashboard_url));
    connection.commit()
    cursor.close()
    connection.close()

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        to_addr=request.form['to_address']
        subject=request.form['subject']
        from_addr=request.form['from_address']
        password=request.form['password']
        dd_public_dashboard_url=request.form['dd_public_dashboard_url']

        if form.validate():
            write_to_db(to_addr, subject, from_addr, password, dd_public_dashboard_url)
            flash('Collected info: {} {} {} {}'.format(to_addr, subject, from_addr, dd_public_dashboard_url))
        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()