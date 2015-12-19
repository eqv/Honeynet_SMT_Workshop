from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    const   = b.Const(100, 64)
    x       = b.Var(64, "x")


    b.Assert(x * 20 == 100)
    b.Assert(b.Ult(x, 100))

    res = b.Sat()
    if res == b.SAT:
        #b.Print_model()
        print("{} {}".format(x.symbol, int(x.assignment,2)))
        #import pdb; pdb.set_trace()
    else: 
        print("unsat")
