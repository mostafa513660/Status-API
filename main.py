from flask import Flask, jsonify, request

app = Flask(__name__)

status = True

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
    app.run(debug=True)
