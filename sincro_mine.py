from mcipc.query import Client # Importamos libreria
from mcipc.rcon.je import Biome, Client

with Client('51.68.206.112', 25591) as client:
    basic_stats = client.stats() # Obtén estadísticas básicas
    full_stats = client.stats(full=True) # Obtenga estadísticas completas

print(basic_stats)
print (full_stats)
