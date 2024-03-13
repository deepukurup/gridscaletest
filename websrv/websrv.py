from flask import Flask, request, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

# Elasticsearch URL
es_url = 'http://elasticsearch.kube-logging.svc.cluster.local:9200'

@app.route('/helloworld/', methods=['POST'])
def hello_world():
    data = request.json
    name = data.get('name', 'World')
    message = f'Hello {name}'

    # Log the request to Elasticsearch
    log_data = {'name': name, 'timestamp': datetime.now().isoformat()}
    requests.post(es_url, json=log_data)

    return jsonify(message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)