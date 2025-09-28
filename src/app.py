from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Gets the hostname of the pod
    pod_name = os.environ.get('HOSTNAME', 'unknown')
    return f"Hello from Pod: {pod_name}!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)