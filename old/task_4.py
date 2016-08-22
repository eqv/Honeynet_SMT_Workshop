from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    input_bits = 8*10 #10 bytes of input
    input = b.Var(input_bits, "input")
    hash  = b.Const(446055857, 32)

    for i in range (0,input_bits):
      hashnew = b.Var(32,"hash"+str(i))
      # hash = if inptu[i]  then hash+136... else hash*308.. end
      b.Assert( hashnew == b.Cond(input[input_bits-i-1], hash + 1364396257, hash*3084817850  ) )
      hash = hashnew

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
