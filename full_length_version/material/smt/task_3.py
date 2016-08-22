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

    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("{} {}".format(x.symbol, int(x.assignment,2)))
        #import pdb; pdb.set_trace()
    else: 
        print("unsat")
