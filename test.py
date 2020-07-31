import requests
data = [{"likes":10,"name":"Saransh","views":4000},
        {"likes":56,"name":"Yaransh","views":77000},
        {"likes":780,"name":"Raransh","views":489000}]

BASE = "http://127.0.0.1:5000/"
for i in range(len(data)):
    response = requests.put(BASE+"video/"+str(i+1),data[i])
    print(response.json())
input()
response = requests.delete(BASE+"video/1")
print(response)
input()
response = requests.get(BASE+"video/1")
print(response.json())

response = requests.get(BASE+"video/2")
print(response.json())

