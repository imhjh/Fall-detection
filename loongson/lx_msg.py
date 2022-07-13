import socket
import os
import sys
import struct
from mail import mail

def socket_service():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #IP For Loongson
    s.bind(('192.168.0.104', 6666))
    s.listen(10)
  except socket.error as msg:
    print(msg)
    sys.exit(1)

  print("Wait..")

  while True:
    sock, addr = s.accept()
    deal_data(sock, addr)
    continue
  s.close()


def deal_data(sock, addr):
  #print("Accept connection from {0}".format(addr))

  while True:
    fileinfo_size = struct.calcsize('128sl')
    buf = sock.recv(fileinfo_size)
    if buf:
      filename, filesize = struct.unpack('128sl', buf)
      fn = filename.decode().strip('\x00')
      new_filename = os.path.join('./', 'new_' + fn)

      recvd_size = 0
      fp = open(new_filename, 'wb')

      while not recvd_size == filesize:
        if filesize - recvd_size != 1024:
          data = sock.recv(1024)
          recvd_size += len(data)
        else:
          data = sock.recv(1024)
          recvd_size = filesize
        fp.write(data)
      fp.close()
    sock.close()
    print("\033[91m%s\033[0m"%"Fall!!!")
    print("Picture received successfully")
    mail()
    break



if __name__ == '__main__':
  socket_service()