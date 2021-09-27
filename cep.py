import urllib.request

zipcode = '60010010'
url = 'https://viacep.com.br/ws/%s/json/' % zipcode
headers = {'User-Agent': 'Autociencia/1.0'}
requisicao = urllib.request.Request(url, headers=headers, method='GET')
cliente = urllib.request.urlopen(requisicao)
endereco = cliente.read().decode('utf-8')
cliente.close()
print(endereco)