import requests

a = requests.post('http://localhost:8000', json={'Insoap': {'words':'тестируем наш веб-сервис. Используем JSON'}})

print(a)
print(a.json())