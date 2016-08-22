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

    #You can use the code below that solves another different hash function as a starting point:
    # HINT: This code JUST HAS A SIMILAR STRUCTURE (loop etc), ITS A COMPLETELY DIFFERENT FUNCTION
    hash  = b.Const(446055857, 32)

    #perform computation on all input bits
    for i in range (0,input_bits):
      hashnew = b.Var(32,"hash"+str(i))
      # hash = if input[i]  then hash+136... else hash*308.. end
      b.Assert( hashnew == b.Cond(input[input_bits-i-1], hash + 1364396257, hash*3084817850  ) )
      hash = hashnew

    #Check that all 8 bit slices of the input are valid bytes
    for i in range(0,input_bits/8):
      o = i * 8
      #all input bytes are from A..Z
      cur = b.Slice(input,o+7, o)
      b.Assert( cur >= 65)
      b.Assert( cur <= 90)

    b.Assert( hash == 2870426180)
    #import pdb; pdb.set_trace()
    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("{} {:x}".format(input.symbol, int(input.assignment,2)))
    else: 
        print("unsat")
