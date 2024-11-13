# binary type data - Bytes
myList=[2,3,4,5,255]
# result=bytes(myList)
# result[0]=56
# print(type(result))

# binary type data - ByteArray

result1=bytearray(myList)
result1[0] = 56
print(result1[0])