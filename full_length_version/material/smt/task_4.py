from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    # Convert the following simple statement into an smt formula
    # char var = input();
    # int val = input();
    # switch( var ){
    #  case( '-' ): v-=1; break; Sub 1 or
    #  case( '*' ): v*=2; break; Multiply with 2
    # }

    #Tip: you can use ord('+') to obtain the ascii value of +

    #import pdb; pdb.set_trace()
    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("{} {:x}".format(input.symbol, int(input.assignment,2)))
    else: 
        print("unsat")
