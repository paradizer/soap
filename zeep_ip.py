from zeep import Client

client = Client('http://www.webservicex.net/geoipservice.asmx?WSDL')
result = client.service.GetGeoIP(
    '82.209.247.130')
print(result)
# assert result == 62.137