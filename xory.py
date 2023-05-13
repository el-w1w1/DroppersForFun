import sys

def xor(data, key): 
    
    out = bytearray(len(data))

    for i in range(len(data)): 
        out[i] = data[i] ^ ord(key[i % len(key)])

    return out


if (len(sys.argv) > 4 or len(sys.argv) < 3): 
    print("bad args")
    sys.exit()

filen = sys.argv[1]

f = open(filen, "rb")
cont = f.read()

out = xor(cont, "YB")


f = open(sys.argv[2], "wb")
f.write(out)


