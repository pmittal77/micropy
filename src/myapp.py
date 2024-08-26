from flask import Flask, jsonify, render_template
import socket


def getHostname():
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    ## printing the hostname and ip_address
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    
    return hostname, ip_address

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(status="Healthy")

@app.route("/details")
def details():
    hostname, ip = getHostname()
    return render_template("index.html", host=(hostname, ip))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

