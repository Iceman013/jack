#import socket module
from socket import *
import sys # In order to terminate the program

import dataStorage

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 1271
#Prepare a sever socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('\nReady to serve...')

    connectionSocket, addr = serverSocket.accept()
    try:
        # Get message
        message = connectionSocket.recv(1024).decode()
        data = message.split()
        
        # Get method type
        method = data[0]
        print(method + " from " + str(addr))
        if (method == "POST"):
            json = data[len(data) - 1]
            dataStorage.storeData(json)
        elif (method == "GET"):
            dataStorage.getData(data[1][1:], connectionSocket)

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode())
        errorMessage = '<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n'
        connectionSocket.send(errorMessage.encode())
        connectionSocket.send(b'\r\n\r\n')

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data