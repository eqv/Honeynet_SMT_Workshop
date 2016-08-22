from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    # Convert the following loop with the body from task_4 to an smt formula
    # and make sure that it returns true. Use the input array given below.
    #
    #uint64_t v = 0;
    #for( int i = 0; i < len; i++ ){
    #   switch( str[i] ){
    #       case( '-' ): v-=1; break; Sub 1 or
    #       case( '*' ): v*=2; break; Multiply with 2
    #       default: return 0;
    #   }
    #}
    #return v == 0xffffffffbadc0de0;

    #Tip: you can use ord('+') to obtain the ascii value of +

    inputlen = 120 #try find a shorter valid input
    #use this array of input values
    inputs = [b.Var(8, "i"+str(i)) for i in range(inputlen)] 
    val = b.Var(64,"val")
    b.Assert(val == 0)

    for i in range(inputlen):
        new_val = b.Var(64, "val"+str(i))
        #not the default case:
        b.Assert( ( inputs[i] == ord('-') ) | (inputs[i]==ord('*') ) )
        #check for *
        elsecase = b.Cond(inputs[i] == ord('*'), val*2, 0)
        #check for -
        switch = b.Cond( inputs[i] == ord('-'), val-1, elsecase)
        #compute new_val from old val
        b.Assert( new_val == switch )
        val = new_val

    b.Assert(val == 0xffffffffbadc0de0)

    #import pdb; pdb.set_trace()
    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("input: {}".format( "".join([str(chr(int(inputs[i].assignment,2))) for i in range(inputlen)])))
    else: 
        print("unsat")
