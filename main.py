from flask import Flask, jsonify

app = Flask(__name__)
api_status = True

@app.route('/api/status', methods=['GET'])
def get_api_status():
    return jsonify({'status': api_status})

@app.route('/api/toggle', methods=['POST'])
def toggle_api_status():
    global api_status
    api_status = not api_status
    return jsonify({'status': api_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
