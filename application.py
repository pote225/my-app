from flask import Flask
application = Flask(__name__) 

@application.route('/hello/<name>') 
def hello(name):
    return 'Hello, World! Hello, ' + name

@application.route('/sum/<inp>') 
def calc(inp):
    return inp + " = " + str(sum(list(eval(inp))))