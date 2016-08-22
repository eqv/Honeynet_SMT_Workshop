from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    #Find out if ((x|y) & ~(x&y))+2*(x&y) always yields the same result as x+y
    #Bonus: find out if (x*x+x)%2 == 0 can be false

    const   = b.Const(100, 64)
    x       = b.Var(64, "x")

    b.Assert(b.Ult(0,x))
    b.Assert(x+5 == 20)

    res = b.Sat()
    if res == b.SAT:
        b.Print_model() #pint all variables as binary
        print("{} {}".format(x.symbol, int(x.assignment,2)))
        #import pdb; pdb.set_trace()
    else: 
        print("unsat")
