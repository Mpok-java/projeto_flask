from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre_o_sistema():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def listar_aluno():
    lista_aluno = [
        (1, 'João', 20, 'São Paulo'),
        (2, 'Maria', 22, 'Rio de Janeiro'),
        (3, 'Pedro', 19, 'Belo Horizonte'),
        (4, 'Ana', 21, 'Teresina'),
        (5, 'Carlos', 23, 'Parnaíba'),
        (6, 'Juliana', 20, 'Picos'),
        (7, 'Lucas', 18, 'Floriano'),
        (8, 'Mariana', 22, 'Campo Maior'),
        (9, 'Gabriel', 19, 'Oeiras'),
        (10, 'Beatriz', 21, 'Piripiri'),
        (11, 'Rafael', 20, 'São Raimundo Nonato'),
        (12, 'Camila', 23, 'Barras'),
        (13, 'Felipe', 18, 'Esperantina'),
        (14, 'Larissa', 22, 'Altos'),
        (15, 'Bruno', 21, 'Pedro II'),
        (16, 'Amanda', 20, 'União'),
        (17, 'Daniel', 19, 'José de Freitas'),
        (18, 'Isabela', 23, 'Bom Jesus'),
        (19, 'Matheus', 18, 'Uruçuí'),
        (20, 'Letícia', 21, 'Corrente'),
        (21, 'Gustavo', 20, 'Imperatriz'),
        (22, 'Sofia', 22, 'São Luís')
    ]
    return render_template('aluno/lista.html', lista_alunos =lista_aluno)


@app.route('/professor')
def lista_professor():
    lista_professor = [
        (1, 'Dr. João Silva', '123.456.789-00', 'MAT001', 'Matemática', 'ejefpookyo@exemplo.com')
            ]
    return render_template('professor/lista.html', lista_professores=lista_professor)


if __name__ == '__main__':
    app.run(debug=True)