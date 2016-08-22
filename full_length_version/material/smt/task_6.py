from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    # Convert the following loop with the body from task_4 to an smt formula
    # and make sure that it returns true. Use the input array given below.
    #
    #uint64_t v = 0;
    #for( int i = 0; i < len; i++ ){
    #   if( str[i] == '-'{
    #       v-=1;
    #   } else {
    #       v*=2; 
    #   }
    #}
    #return v == 0xffffffffbadc0de0;

    #Tip: you can use ord('+') to obtain the ascii value of +

    inputlen = 120 #try find a shorter valid input
    #use this array of input values
    inputs = [b.Var(8, "i"+str(i)) for i in range(inputlen)] 


    #solution of task_4, you might reuse some parts of it
    b.Assert( v_new == b.Cond( input == ord('-'), v-1, v*2 ) )

    #import pdb; pdb.set_trace()
    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("input: {}".format( "".join([str(chr(int(inputs[i].assignment,2))) for i in range(inputlen)])))
    else: 
        print("unsat")
