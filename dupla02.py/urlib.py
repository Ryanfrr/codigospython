from urllib.parse import urlparse
url = 'https://www.piticas.com.br'

url_analisada = urlparse(url)

print(f'Esquema: {url_analisada.scheme}')
print(f'Dominio: {url_analisada.netloc}')