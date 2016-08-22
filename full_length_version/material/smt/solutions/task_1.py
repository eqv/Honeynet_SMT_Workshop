from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)



    # Find int64_t x (e.g. 64 bit signed integer) such that:
    # x < 0
    # x * 133713378 == 13372

    # Tips:
    # a signed less than can be created with b.Slt(x,y)

    const   = b.Const(100, 64)
    x       = b.Var(64, "x")

    b.Assert(b.Slt(x,0))
    b.Assert(x * 133713378 == 13372)

    res = b.Sat()
    if res == b.SAT:
        #b.Print_model()
        print("{} {}".format(x.symbol, int(x.assignment,2)))
        #import pdb; pdb.set_trace()
    else: 
        print("unsat")
