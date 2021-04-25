import time
import socket

from flask import Flask
app = Flask(__name__)
    
@app.route('/pucsd/')
def Time():
    return time.today()

@app.route('/')
def Hostname():
    return socket.hostname()
   
@app.route('/pucsd/')
def City():
    return "Pune"
    
@app.route('/pucsd/')
def Country():
    return "India"
    
@app.route('/pucsd/')
def Region():
    return "Asia"
     
