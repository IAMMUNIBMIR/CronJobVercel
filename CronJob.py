import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # Replace with your authentication details
    auth_url = "https://share.streamlit.io/-/auth/app"
    redirect_uri = "https://app-crypto-3ztzbtrgcfqsnapufmsfbc.streamlit.app/ping"

    # Simulate authentication
    session = requests.Session()
    response = session.get(auth_url, params={'redirect_uri': redirect_uri})

    # Check if authentication is successful
    if response.status_code == 200:
        return jsonify({'status': 'Ping successful'}), 200
    else:
        return jsonify({'status': 'Ping failed'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
