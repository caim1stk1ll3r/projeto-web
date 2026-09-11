from flask import Flask, render_template
from datetime import datetime 

app = Flask (__name__) 

print (__name__)  

@app.route('/') 
def pagina_inicial():
    return '<h1>oieeee</h1><p>Meu primeiro servidor Flask está funcionando.</p>'

# -- ULTIMA COISA DO ARQUIVO

@app.route('/sobre')
def sobre():
    return '''
<h1 style='color:red'>Meu nome é: </h1>
<p>Oliverrrr</p>
<!-- tudo oq eu pensar em html pode vir aki -->
'''

@app.route('/var')
def variavel():
    palavra = 'Oliver'
    return f'<h1>Adicionando texto de var: {palavra}</h1>'

@app.route('/idade/<int:ano>')
def idade(ano):
    calculoIdade = 2026 - ano 
    return f'Você tem {calculoIdade} anos!'

@app.route('/salvar/<nome>/produtos')
def salvar(nome):
    return f'Você salvou o produto [ {nome} ] com sucesso!'

@app.route('/html')
def pagina_html():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    return 'Ainda não tem nada...'

@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18: 
        status = 'Maior de Idade'

    elif idade == 18:
        status = "Maior de Idade"

    else:
        status = 'Menor de Idade - ACESSO NEGADO!'

    return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, nascimento = ano, idade = idade, status = status)

@app.route('/dicio')
def dicionario():
    dados = {
        'chave' : 'valor',
        'curso' : 'GTI',
        'local' : 'fatec jahu',
        'semestre' : 4,    
    }
    return render_template('dicio.html', **dados)

@app.route('/condicao/<int:valor>')
def condicao(valor):
    return render_template('condicao.html', valor = valor)

@app.route('/perfil/<nome>')
def perfil(nome):
    #simulando um banco de dados com um dicionário de usuários
    #na aula 05 isso virá do mysql de vdd
    usuarios = {
        'admin' : {
            'nome' : 'Administrador',
            'email' : 'admin@fatec.br',
            'nivel' : 'administrador',
            'ativo' : True,
            'posts' : 47
        },
        'joao' : {
                'nome' : 'João Silva',
                'email' : 'joa@email.com',
                'nivel' : 'usuario',
                'ativo' : True,
                'posts' : 12
            },
        'admin' : {
                'nome' : 'Maria Souza',
                'email' : 'maria@email.com',
                'nivel' : 'moderador',
                'ativo' : False,
                'posts' : 31
            },
    }

    #busca o usuario pelo nbome na url - .get() retorna None se nao existir
    usuario = usuarios.get(nome)

    #passa o usuario (ou None) para o tempalte
    return render_template('perfil.html', usuario=usuario, nome_buscado=nome)
    




















if __name__ == '__main__':
    app.run(debug=True)