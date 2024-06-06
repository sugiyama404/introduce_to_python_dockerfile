from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def heltch_check():
    return {"answer": "helloworld"}

@app.route('/api', methods=['GET'])
def get_rrder_items():
    return {"answer": "helloworld"}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)
