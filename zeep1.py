from zeep import Client

client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
result = client.service.ConvertSpeed(
    100, 'kilometersPerhour', 'centimetersPersecond')
print(result)
# assert result == 62.137