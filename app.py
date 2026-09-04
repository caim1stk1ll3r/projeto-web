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




















if __name__ == '__main__':
    app.run(debug=True)