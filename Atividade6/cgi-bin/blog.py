#!/usr/bin/env python3
import os
import cgi
import datetime

# Obter os dados enviados pelo formulário
form = cgi.FieldStorage()
name = form.getvalue('name')
message = form.getvalue('message')
date = datetime.datetime.now()
message_data = f' REMETENTE: {name}\tMENSAGEM: {message}\tDATA: {date}\n'
messages = []
messages.append(message_data)
# Armazenar os dados em um arquivo
with open('data/mensagens.txt', 'a', encoding='utf-8') as f:
    f.write(message_data)

# Gerar uma página de confirmação para o usuário
print('Content-type: text/html\n')
"""print('<html>')
print('<head>')
print('  <title>Mensagem Enviada</title>')
print('</head>')
print('<body>')
print('  <h1>Mensagem Enviada</h1>')
print('  <p>Sua mensagem foi enviada com sucesso.</p>')
print('</body>')
print('</html>')""" 

print('<html>')
print('<head>')
print('</head>')
print('<body>')
print('<h1>Página</h1>')
print('  <form method="POST" action="http://localhost:8000/cgi-bin/blog.py"  accept-charset="utf-8">')
print('    <label for="name">Nome:</label><br>')
print('   <input type="text" name="name" id="name"><br>')
print('<br>')
print('<label for="message">Mensagem:</label><br>')
print('<textarea name="message" id="message"></textarea><br>')
print('<br>')
print('<input type="submit" value="Enviarrrrrr">')
print('</form>')

with open('data/mensagens.txt', 'r', encoding='utf-8') as f:
    file = f.readlines()

for line in file:
    data = line.split('\t')
    print(f'  <h1>{data[0]}</h1>')
    print(f'  <p>{data[1]} </p>')
    print(f'<p>{data[2]}</p>')

print('</body>')
print('</html>')