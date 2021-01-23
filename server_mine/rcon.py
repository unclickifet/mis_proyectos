from rcon import Client

with Client('51.68.206.112', 25591) as client:
    response = client.run('some_command', 'with', 'some', 'arguments')

print(response)