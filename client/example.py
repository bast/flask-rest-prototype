import requests


print("testing: starting a calculation")
response = requests.post('http://127.0.0.1:5000/api/v1.0/calculation/start/',
                         json={'model': {'key1': 'value1', 'key2': 'value2'},
                               'parameters': {'key3': 'value3', 'key4': 'value4'}},
                         auth=('someuser', '123456'))
data = response.json()
print(data)


print("testing: getting info about a calculation")
response = requests.get('http://127.0.0.1:5000/api/v1.0/calculation/137/',
                        auth=('someuser', '123456'))
data = response.json()
print(data)


print("testing: modifying a calculation")
response = requests.post('http://127.0.0.1:5000/api/v1.0/calculation/137/',
                        json={'parameters': {'key3': 'value3', 'key4': 'value4'}},
                        auth=('someuser', '123456'))
data = response.json()
print(data)


print("testing: deleting a calculation")
response = requests.delete('http://127.0.0.1:5000/api/v1.0/calculation/137/',
                           auth=('someuser', '123456'))
data = response.json()
print(data)
