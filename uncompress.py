import os
from posixpath import split
import sys

def readFile( str ):
    f = open(str, "rb")
    data = f.read()
    f.close()
    return data

input_file = sys.argv[1]

(filename, ext) = os.path.splitext(input_file)

output_file = filename + '.h'

data = readFile(input_file)
    
print(type(data))

f = open(output_file, "w")
f.write("#pragma once\n")
f.write("const unsigned char VERSION[] = {\"" + filename + "\"};\n")
f.write("const int rknn_size = " + str(sys.getsizeof(data)) + ";\n")
f.write("const unsigned char rknn_data[] = {") #+ str(data, encoding='utf-8') + "\";")
first = True
for i in data:
    if first:
        f.write(hex(i))
        first = False
    else:
        f.write(',' + hex(i))
f.write("};")
f.close()

if(0):
    output_file = filename + "1.gz"
    f = open(output_file, "wb")
    f.write(data_x)
    f.close()