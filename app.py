from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    mensagem = "Hello, World!"
    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    print("Hello, World!")
    app.run(debug=True)