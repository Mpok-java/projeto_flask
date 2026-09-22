from flask import Flask, render_template
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


if __name__ == '__main__':
    app.run(debug=True)