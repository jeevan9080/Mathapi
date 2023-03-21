from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__, template_folder='template')
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "todo.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

def is_armstrong(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/check', methods=['POST'])
def check():
    num = int(request.form['number'])
    if is_armstrong(num):
        message = f"The {num} is Armstrong"
    else:
        message = f"The {num} is not Armstrong"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
