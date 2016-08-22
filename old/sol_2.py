from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    const   = b.Const(133713378, 64)
    x       = b.Var(64, "x")


    b.Assert(x * const == 13372)
    b.Assert(b.Slt(x, 0))

    res = b.Sat()
    if res == b.SAT:
        #b.Print_model()
        print("{} {}".format(x.symbol, int(x.assignment,2)))
    else: 
        print("unsat")
