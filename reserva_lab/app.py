#!/usr/bin/python3


####Teste Vesão 0.1


from flask import Flask, render_template
import socket
IP = [(s.connect(('8.8.8.8', 80)),
       s.getsockname()[0],
       s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adm')
def index():
    return render_template('adm.html')

@app.route('/reserva')
def user():
    return render_template('reserva.html')

@app.route('/cadastro')
def user():
    return render_template('cadastro.html')

@app.route('/consulta')
def user():
    return render_template('consulta.html')

if __name__ == '__main__':
    app.run(debug=True,host=IP)
