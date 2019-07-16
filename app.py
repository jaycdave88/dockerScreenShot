import os 
from flask import Flask, render_template

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'templates')

print(template_dir)

app = Flask(__name__, template_folder="./flask/templates/")
 
 
@app.route('/')
def hello_whale():
    return render_template("jay_test.html")
# def hello_whale():
#     return "hello world"
 
if __name__ == '__main__':
    app.run()