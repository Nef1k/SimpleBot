import json
import random

from flask import Flask, request

from logic.session_storage import SessionStorage

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world', 200


@app.route('/', methods=['POST'])
def vk_request():
    data = json.loads(request.data)
    timestamp = str(random.random)

    SessionStorage.set(timestamp, data)

    return 'ok'


@app.route('/storage', methods=['GET'])
def view_storage():
    storage = SessionStorage.storage
    item_format = '  <li>{item_key}: {item_value}</li>'

    output_html = ['<ul>']
    output_html.extend((item_format.format(
        item_key=key,
        item_value=value
    ) for (key, value) in storage.items()))
    output_html.append('</ul>')

    return '\n'.join(output_html), 200
