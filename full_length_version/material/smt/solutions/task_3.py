from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    # Convert the following C program and finde an input x such that the program returns 1
    # int main(){
    #   uint64_t x = read_uint();
    #   uint64_t a = 0;
    #   a += x;
    #   x = x ^ 0xd701ecf9bd67d788;
    #   a += x;
    #   x = x * 0x94d941135c908617;
    #   a += x;
    #   return a;
    # }

    a = b.Var(64,"a")
    a1 = b.Var(64,"a1")
    a2 = b.Var(64,"a2")
    a3 = b.Var(64,"a3")
    x = b.Var(64,"x")
    x1 = b.Var(64,"x1")
    x2 = b.Var(64,"x2")
    b.Assert(a == 0)
    b.Assert(a1 == a + x)
    b.Assert(x1 == x ^ 0xd701ecf9bd67d788)
    b.Assert(a2 == a1+x1)
    b.Assert(x2 == x1 * 0x94d941135c908617)
    b.Assert(a3 == a2+x2)
    b.Assert(a3 == 1)

    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("{} {}".format(x.symbol, int(x.assignment,2)))
        #import pdb; pdb.set_trace()
    else: 
        print("unsat")
