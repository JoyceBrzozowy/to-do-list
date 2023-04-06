#Este código define uma aplicação Flask com duas rotas: a rota '/' exibe todas as tarefas cadastradas no banco de dados, e a rota '/add' adiciona uma nova tarefa ao banco de dados. A função connect_db é responsável por estabelecer uma conexão com o banco de dados.


from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_secreta'

def connect_db():
    return sqlite3.connect('database.db')

@app.route('/')
def index():
    db = connect_db()
    cur = db.execute('SELECT * FROM tasks ORDER BY id DESC')
    tasks = cur.fetchall()
    db.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    db = connect_db()
    db.execute('INSERT INTO tasks (task) VALUES (?)', [task])
    db.commit()
    db.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



#Para criar o banco de dados, basta executar o seguinte código em Python:

import sqlite3

conn = sqlite3.connect('database.db')
with open('schema.sql') as f:
    conn.executescript(f.read())
conn.close()

#Este código cria um arquivo chamado database.db com a estrutura da tabela tasks definida no arquivo schema.sql.