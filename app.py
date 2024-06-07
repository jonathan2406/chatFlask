from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os
import socket
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SECRET'] = "secret123"
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('message')
def handle_message(message):
    print("Received Message: " + message)
    if message != "User Connected!":
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

def get_public_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    public_ip = get_public_ip()
    socketio.run(app, host=public_ip, port=port)
