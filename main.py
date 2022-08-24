import requests

if __name__ == '__main__':
    url = 'https://api.datos.gob.mx/v1/calidadAire'
    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()
        results = datos['results']
        # print(datos)

for result in results:
    if result["_id"] == "58c780bf281e87010078f491":
        elemento = result
        print(elemento)
        # print(elemento.keys())
        break
elemento = result["stations"][0]["measurements"][0]
myDict = elemento.items()
myList = list(myDict)

measurements = []
medidas = myList[2:]
measurements.append(medidas)
print(measurements)
pollutant = elemento.get('pollutant')
print(pollutant)

"""
endpoint = 'https://api.datos.gob.mx/v1/calidadAire'
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range (200, 299):
    data = r.json()
    results = data['results']
elementoBuscado = []
def BuscarById(myId):
    for result in results:
        if result["_id"] == myId:
            elemento = result["stations"][0]["measurements"][0]
            elementoBuscado.append(elemento)
            print(elementoBuscado)
            # print(type(elementoBuscado))
            return elementoBuscado
BuscarById("58c780bf281e87010078f491")
"""
