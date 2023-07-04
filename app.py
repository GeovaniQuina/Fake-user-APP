from flask import Flask, render_template
import requests
import config

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://api.api-ninjas.com/v1/randomuser'
    response = requests.get(url, headers={'X-Api-key': config.API_KEY}).json()
    if response.get('username'):
        return render_template('index.html', response=response)
    else:
        error_message = f"Error: {response.get('status', '')} - {response.get('message', '')}"
        return error_message

if __name__ == '__main__':
    app.run()
