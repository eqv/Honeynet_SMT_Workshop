#include<stdlib.h>
#include<stdint.h>
#include"llbmc.h"

void test(uint32_t v){
    uint32_t r = v;
    for( int i = 0; i < 32; i++ ){
       r= r ^ (v<<i)*(v+r);
    }
    __llbmc_assert(r!=2016);
}

int main(){
  test(__llbmc_nondef_uint32_t());
  return 0;
}
