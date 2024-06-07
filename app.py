from flask import Flask, render_template
from flask_socketio import SocketIO, send
import os
from flask_cors import CORS
#a
app = Flask(__name__)

app.config['SECRET'] = "secret123";

socketio = SocketIO(app, cros_allowed_orgins="*")


@socketio.on('message')
def handle_message(message):
    print("Received Message: " + message);
    if message != "User Connected!":
        send(message, broadcast=True)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host="https://chatflask-ef559a6c0275.herokuapp.com", port=port)
