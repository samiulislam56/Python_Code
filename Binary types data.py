Samilist = [1,2,3,4,41,54,70,221,255]

b = bytes(Samilist)
print(type(b))

Samilist1 = [1,2,3,4,41,54,70,221,255]
b1 = bytearray(Samilist1)
print(type(b1))

Samilist2 = [1,2,3,4,41,54,70,221,255]
b2 = bytearray(Samilist2)
b2[1] = 100
print(b2[1])