# my-app
My App (my-app)

Step1

Installation
Install python
Install python virtual env
py -m venv env
Install python flask
\Python310\env\Scripts\activate

Development
Create folder my-app-tmp
Write code (application.py)
from flask import Flask
application = Flask(__name__) 

@application.route('/hello/<name>') 
def hello(name):
return 'Hello, World! Hello, ' + name

@application.route('/sum/<inp>') 
def calc(inp):
return inp + " = " + str(sum(list(eval(inp))))

Test in local
set FLASK_APP=application.py
py application.py
py -m flask run

http://127.0.0.1:5000/hello/Milind
http://127.0.0.1:5000/sum/12.2,12

Step2
Create repository as my-app in github
Sync using below commands
git clone <>/my-app
move from my-app-tmp to my-app
git add –all
git commit
git push

