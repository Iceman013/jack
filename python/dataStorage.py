storage = []

def storeData(json):
    storage.append(json)

def getMatching(url):
    output = []
    for i in storage:
        data = i[1:len(i) - 1].split(",")
        if (data[0][0:6] == '"game"'):
            if (data[0][8:len(data[0]) - 1] == url):
                output.append(i)
    return output
        
def getData(url, connectionSocket):
    connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
    
    targetData = getMatching(url)
    
    for i in targetData:
        connectionSocket.send(i.encode())
        connectionSocket.send(b',\n')