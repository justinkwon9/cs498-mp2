from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip():
	hostname = socket.gethostname()
	ip_add = socket.gethostbyname(hostname)
	return ip_add

@app.route('/', methods=['POST'])
def run_stress():
	subprocess.Popen(["python3", "stress_cpu.py"])
	return "CPU Stress File Running", 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
