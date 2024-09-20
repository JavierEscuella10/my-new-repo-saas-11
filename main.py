from flask_cors import CORS
from flask import Flask


app = Flask(__name__)

CORS(app)


@app.route("/test_endpoint",methods=['GET'])
def test_function():
    print("HELLOO THIS IS SUCCESSFULL")
    return "HELLO THIS IS SUCCESSFULL"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)