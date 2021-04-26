from datetime import datetime
import socket

from flask import Flask
app = Flask(__name__)

@app.route('/pucsd/')
def myapp():
    hostname = socket.gethostname()
    return {"Time":datetime.now(), "IP Address":socket.gethostbyname(hostname), "Hostname":hostname, "City":"Pune", "Country":"India", "Region":"Asia"}

if __name__ == '__main__':
    app.run(port=5000)
