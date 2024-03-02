#websrv.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/helloworld/', methods=['POST'])
def hello_world():
    data = request.get_json()
    name = data.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#testing the code :- curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"Alice\"}" http://127.0.0.1:5000/helloworld/