from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

status = True

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host_ip = s.getsockname()[0]
        s.close()
        return host_ip
    except Exception as e:
        print(f"Error getting host IP: {e}")
        return '127.0.0.1'

@app.route('/get_status', methods=['GET'])
def get_status():
    client_ip = request.remote_addr
    return jsonify({'status': status})

@app.route('/toggle_status', methods=['POST'])
def toggle_status():
    global status
    status = not status
    client_ip = request.remote_addr
    return jsonify({'status': status})

if __name__ == '__main__':
    print(get_host_ip())
    app.run(host=host_ip, port=5000, debug=True)
    
