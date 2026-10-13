from flask import Flask, render_template, request
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre_o_sistema():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista = lista)


@app.route('/professor')
def lista_professor():
    dao = ProfessorDAO()
    lista_professor = dao.listar()
    return render_template('professor/lista.html', lista=lista_professor)


@app.route('/turma')
def lista_turma():
    dao = TurmaDAO()
    lista_turma = dao.listar()
    return render_template('turma/lista.html', lista=lista_turma)


@app.route('/curso')
def lista_curso():
   dao = CursoDAO()
   lista_curso =dao.listar()
   return render_template('curso/lista.html', lista=lista_curso)
   #return render_template('curso/lista.html')


@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
    return render_template('saudacao/saudacao.html' )

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    dados = f"Usuário: {usuario}, Senha: {senha}, Email: {email}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)


@app.route('/desafio')
def desafio1():
    return render_template('desafio/desafio.html', valor_recebido="Desafio 1")

@app.route('/cadastro', methods=['POST'])
def luz_desafio():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    cpf = request.form['cpf']
    nome_mae = request.form['nome_mae']
    return render_template('cadastro/cadastro.html', nome=nome, data_nascimento=data_nascimento, cpf=cpf, nome_mae=nome_mae)
if __name__ == '__main__':
    app.run(debug=True)