from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://chatflask-ef559a6c0275.herokuapp.com"}})  # Configuración de CORS

app.config['SECRET'] = "secret123"

socketio = SocketIO(app, cors_allowed_origins="https://chatflask-ef559a6c0275.herokuapp.com")  # Configuración de SocketIO con CORS

@socketio.on('message')
def handle_message(message):
    print("Received Message: " + message)
    if message != "User Connected!":
        send(message, broadcast=True)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host="0.0.0.0", port=port)
