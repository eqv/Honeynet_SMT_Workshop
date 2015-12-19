def hash_func(inputstr):
    crc = 0
    mask = 0x04C11DB7
    i = 0
    for bit in inputstr:
        print "in bit: {} with crc bit{}".format(int(bit),int("{:032b}".format(crc)[0]))
        if int(bit) == int("{:032b}".format(crc)[0]):
            crc = (crc << 1)&0xffffffff
        else:
            crc = ((crc<<1)^mask)&0xffffffff
        print("{}: {:032b}".format(i,crc))
        i+=1
    return crc

def bitstring(str):
    bitstring = ""
    for c in str:
        bitstring+= "{:08b}".format(ord(c))
    return bitstring

print hash_func(bitstring("<+->"))
