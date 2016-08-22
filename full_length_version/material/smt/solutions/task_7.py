from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    #Find an input string str such that hash(bitstring(str)) == 0
    #You find the implementation of hash in task_6_hash.py and you should use the outputs produced by it to
    #debug your program if there are any problems.

    #Tip: Introduce additional variables that will be printed to find out what is going on in your formula
    #Tip: You can get the ith-bit of an integer by using var[i], starting from the least significant bit (e.g. var[0] will return the lsb)

    #We use one big integer instead of an array of chars because crc will only use one bit at a time
    input_bits = 8*20 #20 bytes of input
    input = b.Var(input_bits, "input") # a long bitstring


    mask  = b.Const(0x04C11DB7, 32)
    crc = b.Const(0, 32)

    for i in range (0,input_bits):
      crc_new = b.Var(32,"crc"+str(i))

      #debug values
      inputbit = b.Var(1, "inputbit"+str(i))
      crcbit = b.Var(1, "crcbit"+str(i))
      b.Assert( inputbit == input[input_bits-i-1] )
      b.Assert(crcbit == crc[31])

      is_equal = input[input_bits-i-1] == crc[31]

      b.Assert( crc_new == b.Cond(is_equal, (crc<<1), (crc<<1)^mask ) )
      crc = crc_new

    b.Assert(crc == 0)

    for i in range(0,input_bits/8):
      o = i * 8
      #all input bytes are from A..Z
      cur = b.Slice(input,o+7, o)
      b.Assert( 
                (cur == ord('+'))|
                (cur == ord('-'))|
                (cur == ord('<'))|
                (cur == ord('>'))|
                (cur == ord(';'))|
                (cur == ord(' '))
               ) 

    #import pdb; pdb.set_trace()
    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("{} {:x}".format(input.symbol, int(input.assignment,2)))
    else: 
        print("unsat")
