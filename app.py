from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

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
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    #print(form.errors)
    if request.method == 'POST':
        to_addr=request.form['to_address']
        subject=request.form['subject']
        from_addr=request.form['from_address']
        password=request.form['password']
        dd_public_dashboard_url=request.form['dd_public_dashboard_url']

        if form.validate():
            # write_to_disk(name, surname, email)
            flash('Collected info: {} {} {} {}'.format(to_addr, subject, from_addr, dd_public_dashboard_url))

        else:
            flash('Error: All Fields are Required')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()