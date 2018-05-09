import socket
import struct
import time

'''
  https://tools.ietf.org/html/rfc1350

  opcode  operation
    1     Read request (RRQ)
    2     Write request (WRQ)
    3     Data (DATA)
    4     Acknowledgment (ACK)
    5     Error (ERROR)

'''

UDP_IP = "127.0.0.1"
UDP_PORT = 69
FILENAME = "sample.txt"

print("UDP target IP: %s"%UDP_IP)
print("UDP target port: %d"%UDP_PORT)
print("message: %s"%FILENAME)

FN = bytes(FILENAME.encode('ascii'))
MODE = bytes('netascii'.encode('ascii'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, 0))           #zero significa qualquer
RCV_PORT = sock.getsockname()[1] #obtem a porta selecionada

MSG = struct.pack(">H%dsB%dsB"%(len(FN),len(MODE)),1,FN,0,MODE,0)
sock.sendto(MSG, (UDP_IP, UDP_PORT))

time.sleep(2)

data, addr = sock.recvfrom(512)
print(data)
print(len(data))

OPTO,BLK_N,FILE_RCV = struct.unpack('>HH%ds'%(len(data)-4),data)
print('opto code: %d'%OPTO)
print('block number: %d'%BLK_N)
print('file: %s'%FILE_RCV)

#MSG = struct.pack(">HH",3,BLK_N)
#sock.sendto(MSG, (UDP_IP, UDP_PORT))


