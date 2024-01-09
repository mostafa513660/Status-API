from flask import Flask

app = Flask(__name__)

@app.route('/check_api', methods=['GET'])
def check_api():
    result = True
    return str(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
