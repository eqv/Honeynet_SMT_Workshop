#include<stdlib.h>
#include<string.h>
#include"llbmc.h"

typedef struct Entry {
  int val;
} entry_t;

entry_t* NewEntry(int val){
  if(val < 0 ){return NULL;}
  entry_t* res = (entry_t*)malloc(sizeof(entry_t));
  res->val = val;
  return res;
}

typedef struct RingBuffer {
  int size;
  int offset;
  entry_t** buffer;
} ringbuffer_t;

ringbuffer_t* NewRingBuffer(int size){
  if(size<1){return NULL;}
  ringbuffer_t* buf = (ringbuffer_t*)malloc(sizeof(ringbuffer_t));
  buf->size = size;
  buf->offset = 0;
  buf->buffer = malloc(size*sizeof(entry_t*));
  for(int i = 0; i < size; i++){
    buf->buffer[i] = NULL;
  }
  return buf;
}

entry_t* GetElement(ringbuffer_t* buf){
  return buf->buffer[ (buf->offset) % buf->size];
}

void Advance(ringbuffer_t* buf, int amount){
  //avoid integer overflow in addition
  amount = amount % buf->size;
  if(amount < 0 ){amount += buf->size;}
  __llbmc_assert(amount >= 0);
  buf->offset = (buf->offset+amount)%buf->size;
}

void Drop(ringbuffer_t* buf, int amount){
  if(amount < 0 || amount > buf->size){return;}
  Advance(buf, -amount);
  for(int i = 0; i <= amount; i++){
    if(buf->buffer != NULL){
      free(buf->buffer[(buf->offset+i)% buf->size]);
      buf->buffer[(buf->offset+i) % buf->size] = NULL;
    }
  }
}

void Replace(ringbuffer_t* buf, entry_t* val){
  entry_t* old = GetElement(buf);
  __llbmc_assert(buf->offset >=0 );
  __llbmc_assert(buf->offset < buf->size );
  if(old != NULL) free(old);
  if(val != NULL){
    buf->buffer[buf->offset] = val;
  } else { 
    old = NULL; 
  }
}

#define read_int __llbmc_nondef_int

void test(int advance, int amount){
  ringbuffer_t* buf = NewRingBuffer(2);
  Advance(buf, advance);
  GetElement(buf);
  Drop(buf, amount);
}

int main(){
  test(read_int(), read_int());
  return 0;
}
