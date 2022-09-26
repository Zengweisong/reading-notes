import struct

F = open('data.bin', 'wb')
data = struct.pack('>i4sh', 7, b'spam', 8)
print(data)  #b'\x00\x00\x00\x07spam\x00\x08'
F.write('data')
F.close()
F = open('data.bin', 'rb')
data = F.read()
print(data)  #b'\x00\x00\x00\x07spam\x00\x08'
values = struct.unpack('>i4sh', data)  #(7, b'spam', 8)
print(values)