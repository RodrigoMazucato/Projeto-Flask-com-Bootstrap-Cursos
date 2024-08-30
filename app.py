from flask import Flask, render_template
from extrair_textos import *

app = Flask(__name__)

@app.route('/')
def exibir_projeto():
    return render_template('index.html', cursos=extrair_descricao_cursos('textos/descricao_cursos'))

if __name__ == '__main__':
    app.run(debug=True)