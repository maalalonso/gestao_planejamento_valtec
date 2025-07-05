from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Gestão Planejamento Valtec</h1><p>Página inicial do sistema.</p>"

if __name__ == "__main__":
    app.run()
