#!/usr/bin/env python3
import os
import cgi
import datetime

# Obter os dados enviados pelo formulário
form = cgi.FieldStorage()
name = form.getvalue('name')
message = form.getvalue('message')
date = datetime.datetime.now()

# Armazenar os dados em um arquivo
with open('data/mensagens.txt', 'a', encoding='utf-8') as f:
    f.write(f'DATA: {date}\nREMETENTE: {name}\nMENSAGEM: {message}\n\n')

# Gerar uma página de confirmação para o usuário
print('Content-type: text/html\n')
print('<html>')
print('<head>')
print('  <title>Mensagem Enviada</title>')
print('</head>')
print('<body>')
print('  <h1>Mensagem Enviada</h1>')
print('  <p>Sua mensagem foi enviada com sucesso.</p>')
print('</body>')
print('</html>')
