import csv

import socket
TCP_IP = '10.0.0.15'
TCP_PORT = 61557
BUFFER_SIZE = 1024
ifile  = open('data_50.csv', "r")
read = csv.reader(ifile)
#print(read[0])
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))

for row in read :
    print ("Force vector x: " +row[3])
 #   s.send(row[3])
    print ("Force vector y: " +row[4])
    print ("Force vector z: "+ row[5])
    print()
