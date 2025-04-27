from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    mensagem = "Hello, World!"  # A mensagem para passar para o HTML
    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    print("Hello, World!")  # Isso será impresso no terminal quando o servidor for iniciado
    app.run(debug=True)