storage = []

def storeData(json):
    storage.append(json)
    
def getData(url, connectionSocket):
    connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
    for i in range(0, len(storage)):
        connectionSocket.send(storage[i].encode())
        connectionSocket.send(b',\n')