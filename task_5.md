In the last exercise we have seen that SMT solvers can be used to unroll loops
in programs to find if certain program states are reachable (e.g. can we reach
a state where the `hash` variable contains the value 0). This can be automatized (e.g. for C programs) and more complex questions can be asked. A tool that performs such an analysis is LLBMC. LLBMC takes llvm bytecode and tries to find program paths that lead to problematic behaviour (such as invalid pointer usage, double free, integer overflows). 

We will now use LLBMC to get hired at
(https://www.reddit.com/r/netsec/comments/1nw87h/rnetsecs_q4_2013_information_security_hiring/cct1tri)
(not really, we are just going to identify the bugs without hard thinking).

The C code in question is:

```C
//task_5.c
#include <stdlib.h>
#include <stdio.h>

int * allocate_and_fill(int numberOfElements, int magic){
    int *buff;
    unsigned int i, j;

    if(numberOfElements > 4096)
        return((int *)0);    
    j=numberOfElements;
    buff=(int *)malloc(j * sizeof(int));
    if(!buff)
        return((int *)0);

    for(i=0; i<j; i++)
        buff[i]=magic;

    fprintf(stdout, "%08x\n", buff[numberOfElements - 1]);
    return(buff);
}
```

We will now add a harness such that LLBMC is able to analyze the given code.
LLBMC needs a main function. It allows us to create undefined values of the
usual integer types via `__llbmc_nondef_unsigned_short_int` et. al. These functions are defined in llbmc.h in the examples folder of the llbmc download, you need to include it.

__Create a Main function that calls `allocate_and_fill` with two nondef values.__

__Create llvm bytecode for this program with:__

```
clang -c -g -emit-llvm -I. test.c -o test.bc
```


You can then use llbmc to find problematic inputs.

You can exclude certain inputs by using the assume makro `assume(len != 0);`

Eventually the analysis will not finish because the loop count needs to
be too big. __What can you do to still obtain a positive result?__
