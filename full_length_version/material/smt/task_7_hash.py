

def hash_func(inputstr):
    crc = 0
    mask = 0x04C11DB7
    i = 0
    print inputstr
    for bit in inputstr:
        print "in bit: {} with crc bit {}".format(int(bit),most_significant_bit(crc))
        if int(bit) == most_significant_bit(crc):
            crc = (crc << 1)&0xffffffff
        else:
            crc = ((crc<<1)^mask)&0xffffffff
        print("{}: {:032b}".format(i,crc))
        i+=1
    return crc

# return 1/0 corresponding to the highest bit in an 32 bit integer
def most_significant_bit(integer):
    return int("{:032b}".format(integer)[0])

#Converst an ascii string "ab" to the string containing only the bits "11000011100010"
def bitstring(str):
    bitstring = ""
    for c in str:
        bitstring+= "{:08b}".format(ord(c))
    return bitstring

def hex_to_string(hexstring):
    hexstring.decode("hex")

print hash_func(bitstring(hex_to_string("6161")))
