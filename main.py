from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

status = True

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to Google's public DNS server
        host_ip = s.getsockname()[0]
        s.close()
        return host_ip
    except Exception as e:
        print(f"Error getting host IP: {e}")
        return '0.0.0.0'  # Default to all available network interfaces

@app.route('/get_status', methods=['GET'])
def get_status():
    client_ip = request.remote_addr
    print(f"Request from IP: {client_ip}")
    return jsonify({'status': status})

@app.route('/toggle_status', methods=['POST'])
def toggle_status():
    global status
    status = not status
    client_ip = request.remote_addr
    print(f"Toggle request from IP: {client_ip}")
    return jsonify({'status': status})

if __name__ == '__main__':
    host_ip = get_host_ip()
    print(f"API running at http://{host_ip}:5000/")
    app.run(host='0.0.0.0', port=5000, debug=True)
