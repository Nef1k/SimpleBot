from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world', 200


@app.route('/', methods=['POST'])
def vk_confirmation():
    return '44b39bae'
