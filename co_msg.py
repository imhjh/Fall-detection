import socket
import os
import sys
import struct


def sock_client():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #IP For Loongson
    s.connect(('192.168.0.104', 6666))
  except socket.error as msg:
    print(msg)
    print(sys.exit(1))

  while True:
    filepath = 'photo.jpg'
    fhead = struct.pack(b'128sl', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(filepath).st_size)
    s.send(fhead)
    print('Sending: {0}'.format(filepath))

    fp = open(filepath, 'rb')
    while 1:
      data = fp.read(1024)
      if not data:
        print('{0} Send over'.format(filepath))
        break
      s.send(data)
    s.close()
    break


if __name__ == '__main__':
  sock_client()