import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    # URLs of the Streamlit apps to ping
    urls_to_ping = [
        "https://iammunibmir-weather-forecast-app-main-zzt3wh.streamlit.app/",
        "https://app-crypto-3ztzbtrgcfqsnapufmsfbc.streamlit.app/"
    ]
    
    responses = []
    for url in urls_to_ping:
        try:
            # Simulate authentication
            auth_url = "https://share.streamlit.io/-/auth/app"
            session = requests.Session()
            response = session.get(auth_url, params={'redirect_uri': url})

            # Check if authentication is successful
            if response.status_code == 200:
                responses.append({'url': url, 'status': 'Ping successful'})
            else:
                responses.append({'url': url, 'status': 'Ping failed', 'code': response.status_code})
        except Exception as e:
            responses.append({'url': url, 'status': 'Ping failed', 'error': str(e)})

    return jsonify(responses), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)