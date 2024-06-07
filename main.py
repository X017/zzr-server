from bottle import *
import os 
import random 
import string 
import time 
import json 
import sqlite3

app = Bottle()
addrFile = 'files/'
userpw = 'users/'

#sdb = sqlite3.connect('db')
def randz(seed): #link randomizer
    rz = ''
    for i in range(seed):
        rz = rz + random.choice(string.ascii_letters)
    return rz


fileAddress = randz(5)


@get('/login')
def loginGet():
    return template('login.tpl')

@post('/login')
def loginData():
    global username
    global password
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == 'admin' and password == '25df':
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
    redirect('/list')


@get('/list')
def fileDir():
    listData = []
    for file in os.listdir('files'):
        listData.append(file)
    return template("file.tpl",data=listData)


@get('/upload')
def upload_page():
    try:
        if username == 'admin' and password == '25df':
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
    



run(host='localhost',port=7000,reloader=True)

