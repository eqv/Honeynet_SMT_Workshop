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

    var = b.Var(8,"var")
    val = b.Var(32,"val")
    val_new = b.Var(32,"val_new")
    then_case= val - 1
    else_case= b.Cond(val == ord('*'), val*2, val)
    switch = b.Cond(var == ord('-'), then_case, else_case)
    b.Assert( val_new == switch )
    b.Assert( val_new != val)

    #import pdb; pdb.set_trace()
    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
    else: 
        print("unsat")
