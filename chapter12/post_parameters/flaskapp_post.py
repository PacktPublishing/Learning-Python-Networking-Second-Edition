#!/usr/local/bin/python3

from flask import Flask, request, render_template
import json

app = Flask(__name__)
app.debug = True

@app.route('/',methods=['GET'])
def index():
        return render_template('index.html')

@app.route('/validate',methods=['POST'])
def validate():
        user = request.form['user']
        password = request.form['password']
        if user == 'admin' and password == 'password':
                response = {'user_validate':True,'message':'User authenticated'}
        else:	
                response = {'user_validate':False,'message':'User incorrect'}
        return json.dumps(response)

if __name__ == '__main__':
        app.run()