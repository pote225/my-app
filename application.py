from flask import Flask
application = Flask(__name__) 

@application.route('/hello/<name>') 
def hello(name):
    return 'Hello, World! Github Actions. Hello, ' + name

@application.route('/sum/<inp>') 
def calc(inp):
    return 'sum(' inp + ') = ' + str(sum([float(i) for i in inp.split(',')]))
