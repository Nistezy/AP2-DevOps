from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return document.write('Hello, World!')
if __name__ == '__main__':
    app.run()