from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def current_time():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'The current time is: {now}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
