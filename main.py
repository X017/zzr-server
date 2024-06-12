
from bottle import *
import os 
import random 
import string 
import time 
import json 
import sqlite3 

app = Bottle()
addrFile = 'files/'
userdir = 'users/'

def userHandler(name, mode): 
    #tbh idk what to do anymore i just make it work.
    path = userdir+name+'.json'
    try:
        if mode == 'r':
            with open(path,mode) as f:
                return f.read()
        else:
            pass
    except FileNotFoundError:
        redirect('login') 


@get('/login')
def loginGet():
    return template('login.tpl')

@get('/')
def indexGet():
    redirect('/login')


@post('/login')
def loginData():
    global username,password,data
    username = request.forms.get('username')
    password = request.forms.get('password')
    data = json.loads(userHandler(username,'r')) 


    if username == data['name'] and password == data['password']:
        redirect('upload')
    else:
        return {'ERROR':"WRONG PASSWORD! TRY AGAIN"}

@get('/raw/<fileName>')
def rawGet(fileName):
    try:
        if fileName in os.listdir('files'):
            file = addrFile + fileName
            with open(file,'r') as rf:
                return rf.read()
        else:
            return ''' <title> File Not Found!</title>
                       <p1>File Not Found 404!</p1>
            '''
    except NameError:
        redirect('/login')

@get('/raw')
def rawredirect():
    redirect('list')


@get('/list')
def fileDir():
    listData = []
    for file in os.listdir('files'):
        listData.append(file)
    return template("file.tpl",data=listData)


@get('/upload')
def upload_page():
    try:
        if username == data['name'] and password == data['password']:
            return template('upload.tpl')
        else:
            redirect('login')
    except NameError:
        redirect('login')


@route('/upload',method='POST')
def do_upload():
        try:
            upload = request.files.get('upload')
            save_path = 'files'
            upload.save(save_path)
            return "File Uploaded!"

        except IOError:
            return '''
                    <html> 
                            <h1> File Already Exists! </h1>
                    </html>
            '''
    


dbHandler()
run(host='localhost',port=7000,reloader=True)

