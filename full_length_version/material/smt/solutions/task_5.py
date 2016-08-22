from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    # Convert the following loop with to an smt formula
    #
    #uint32_t v = reead_uint();
    #uint32_t r = v;
    #for( int i = 0; i < 32; i++ ){
    #   r= r ^ (v<<i)*(v+r);
    #}
    #// r == 2016


    v = b.Var(32,"v")
    r = b.Var(32,"r")
    b.Assert(r == v)

    for i in range(32):
        r_next = b.Var(32, "r"+str(i))
        b.Assert(r_next == r ^ (v<<i)*(v+r))
        r = r_next

    b.Assert(r == 2016)

    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("{} {}".format(v.symbol, int(v.assignment,2)))
    else: 
        print("unsat")
