from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__mane__':
    app.run()