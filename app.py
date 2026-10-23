from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)
app.secret_key = "KAMEHAMEHAMEHA_GENKI_DAMA"

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


@app.route('/aluno/form')
def form_aluno():
    return render_template('aluno/form.html', aluno = None)


@app.route('/aluno/salvar/', methods=['POST'])
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    resultado = dao.salvar(id, nome, idade, cidade)
    if resultado['status'] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/aluno')


@app.route('/professor')
def lista_professor():
    dao = ProfessorDAO()
    lista_professor = dao.listar()
    return render_template('professor/lista.html', lista=lista_professor)


@app.route('/professor/form')
def form_professor():
    return render_template('professor/form.html', professor = None)


@app.route('/professor/salvar/', methods=['POST'])
def salvar_professor(id=None):
    nome = request.form['nome']
    disciplina = request.form['disciplina']
    dao = ProfessorDAO()
    resultado = dao.salvar(id, nome, disciplina)
    if resultado['status'] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/professor')


@app.route('/turma')
def lista_turma():
    dao = TurmaDAO()
    lista_turma = dao.listar()
    return render_template('turma/lista.html', lista=lista_turma)


@app.route('/turma/form')
def form_turma():
    return render_template('turma/form.html', turma = None)


@app.route('/turma/salvar/', methods=['POST'])
def salvar_turma(id=None):
    semestre = request.form['semestre']
    curso = request.form['curso']
    professor = request.form['professor']
    dao = TurmaDAO()
    resultado = dao.salvar(id, semestre, curso, professor)
    if resultado['status'] == "ok":
        flash("Turma salva com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/turma')


@app.route('/curso')
def lista_curso():
   dao = CursoDAO()
   lista_curso =dao.listar()
   return render_template('curso/lista.html', lista=lista_curso)
   #return render_template('curso/lista.html')


@app.route('/curso/form')
def form_curso():
    return render_template('curso/form.html', curso = None)


@app.route('/curso/salvar/', methods=['POST'])
def salvar_curso(id=None):
    nome_curso = request.form['nome']
    duracao = request.form['duracao']
    dao = CursoDAO()
    resultado = dao.salvar(id, nome_curso, duracao)
    if resultado['status'] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/curso')


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


