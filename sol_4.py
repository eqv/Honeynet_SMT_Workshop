from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    input_bits = 8*13
    input = b.Var(input_bits, "input")
    mask  = b.Const(0x04C11DB7, 32)
    hash  = b.Const(0, 32)

    for i in range (0,input_bits):
      hashnew = b.Var(32,"hash"+str(i))
      b.Assert( hashnew == b.Cond( input[input_bits-i-1] == hash[31], hash << 1, (hash << 1)^mask  ) )
      hash = hashnew

    for i in range(0,input_bits/8):
      o = i * 8
      cur = b.Slice(input,o+7, o)
      b.Assert( (cur == ord('+')) | (cur == ord('-')) | (cur == ord('<')) | (cur == ord('>'))| (cur == ord(';')) | (cur == ord(' ')))

    b.Assert( crc == 0)

    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("{} {:x}".format(input.symbol, int(input.assignment,2)))
    else: 
        print("unsat")
