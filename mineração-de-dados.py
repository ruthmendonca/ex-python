from bs4 import BeautifulSoup as BS
import requests
import re
from time import sleep

#Página principal
url = 'https://www.estantevirtual.com.br/estante'
requisição = requests.get(url)
conteúdo = BS(requisição.text)

  #Coletar os dados dos grupos de livros
mural = list()
for i in conteúdo.find_all(class_="container_estante-icons"):
  mural = i.get_text(",", strip=True).split(",")

  #Coletar os gêneros e seus links
categorias = list()
urls = list()

for i in conteúdo.find_all(class_='estantes-list'):
  db = i.find_all("a")
  link_regex = re.compile(r"https.*")
  link = link_regex.findall(str(db).replace('">', ''))
 # print(link)

  #Adição doss gêneros e links em suas respectivas listas
  categorias.append(i.get_text(",", strip = True).split(","))
  urls.append(link)

print("-="*28)
print(f'''
FONTE: https://www.estantevirtual.com.br/estante
Na mineração de dados foram encontrados {len(categorias)} categorias''')

c = 0
for i in mural:
  print(f'[{c}]: {i}')
  c+= 1
print("")
categoria = int(input(f'''Qual categoria deseja analisar?
'''))
print("")
print("-="*28)
print("")
print(f"A categoria escolhida foi: '{mural[categoria]}'")
print(f'''
A categoria possuí {len(categorias[categoria])} gêneros''')

g = 0
for i in categorias[categoria]:
  print(f'[{g}]: {i}')
  g += 1
print("")
gênero = int(input(f'''Qual gênero deseja analisar?
'''))
print("")
print("-="*28)
print("")
print(f"O gênero escolhido foi: '{categorias[categoria][gênero]}'")
print("")
print("-="*28)
print("")
sleep(1)
print("Procurando...")


#Página Secundária
requisição2 = requests.get(urls[categoria][gênero])
conteúdo2 = BS(requisição2.text)

títulos = list()
for i in conteúdo2.find_all("h2"):
   títulos.append(i.get_text(" ", strip=True))

print(f'Foram encontrados: {len(títulos)} títulos')
print(f"Os títulos disponíveis são: {títulos}")
print("-="*28)
print("")
