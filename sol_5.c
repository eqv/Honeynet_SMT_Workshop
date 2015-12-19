#include <stdlib.h>
#include <stdio.h>
#include "llbmc.h"

int * allocate_and_fill(int numberOfElements, int magic){
    int *buff;
    unsigned int i, j;

    if(numberOfElements > 50)
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

int main(int argc, char *argv[]) {
  int len = __llbmc_nondef_int();
  assume(len > 0);
  allocate_and_fill( len, __llbmc_nondef_int() );
  return 0;
}
