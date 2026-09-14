from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre_o_sistema():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def listar_aluno():

    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT id, nome, idade, cidade FROM aluno')

    lista = cursor.fetchall()

    conn.close()
    
    return render_template('aluno/lista.html', lista =lista)


@app.route('/professor')
def lista_professor():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, disciplina FROM professor')
    lista_professor = cursor.fetchall()
    conn.close()

    return render_template('professor/lista.html', lista=lista_professor)


if __name__ == '__main__':
    app.run(debug=True)