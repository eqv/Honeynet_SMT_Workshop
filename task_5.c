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
