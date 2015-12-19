from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    x       = b.Var(64, "x")
    y       = b.Var(64, "y")

    b.Assert( b.Not(((x | y) & ~(x & y)) + 2*(x&y) == x+y) )

    #import pdb; pdb.set_trace()
    res = b.Sat()
    if res == b.SAT:
        #b.Print_model()
        print("{} {}".format(x.symbol, int(x.assignment,2)))
    else: 
        print("unsat")
