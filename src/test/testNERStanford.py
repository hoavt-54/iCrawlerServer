'''
Created on Dec 11, 2015

@author: hoavu
'''
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8080))
data = "In order to avoid further proliferation to armed groups in the"\
    " region and the misuse of these weapons by groups like ISIS, Amnesty International"\
    " is calling for supplier states, including the U.S., to work with Iraqi authorities "\
    "to quickly implement stricter controls on the transfer, storage and deployment of arms.\n"
clientsocket.send(data.encode())
print(clientsocket.recv(512).decode())