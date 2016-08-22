from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    #Find out if ((x|y) & ~(x&y))+2*(x&y) always yields the same result as x+y
    #Bonus: find out if (x*x+x)%2 == 0 can be false

    x       = b.Var(64, "x")
    y       = b.Var(64, "y")

    #should be unsat
    b.Assert( b.Not( (( (x|y) & ~(x&y))+2*(x&y)) == x+y))

    #bonus
    #b.Assert( b.Not( (x*x+x)%2 == 0 ))

    res = b.Sat()
    if res == b.SAT:
        b.Print_model() #pint all variables as binary
        print("{} {}".format(x.symbol, int(x.assignment,2)))
        #import pdb; pdb.set_trace()
    else: 
        print("unsat")
