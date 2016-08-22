SMT solvers are very powerful tools. They are capable of solving incredible
complex formulas (think: many MB of formulas). They are able to 'learn'
internal details of the formula and thus solve many instances in milliseconds,
even if the searchspaces are gigantic. In generall you can assume
that if there is a way of solving a problem efficiently, SMT solvers will
solve the encoding in SMT-formulas efficiently. However there are examples where SMT solvers
will be rather slow. Take for example a simple numerical problem: Find two
notrivial (e.g. not 1) factors `p`,`q` such that `p*q = 6261023852299712549`. With
our SMT solver this problem will take a very long time to solve, since the
under laying problem is "breaking RSA" which is hard. However there are
specialized programs that will solve this factorization problem in
milliseconds.  Non the less, SMT solvers can be used to attack cryptographic
problems if the crypto is implemented weakly. 

In this task we will use SMT
solvers to find preimages for a weak hash function. To make it a bit more
interesting we will constrain the input char set to `"+-><; "`. The hash
function in question is a version of crc32. The input restriction makes it harder
to use of the shelf crc32 preimage tools.

```python
#taskt_4_hash.py
def hash_func(inputstr):
    crc = 0
    mask = 0x04C11DB7
    i = 0
    for bit in inputstr:
        print "in bit: {} with crc bit{}".format(int(bit),int("{:032b}".format(crc)[0]))
        if int(bit) == int("{:032b}".format(crc)[0]):
            crc = (crc << 1)&0xffffffff
        else:
            crc = ((crc<<1)^mask)&0xffffffff
        print("{}: {:032b}".format(i,crc))
        i+=1
    return crc

def bitstring(str):
    bitstring = ""
    for c in str:
        bitstring+= "{:08b}".format(ord(c))
    return bitstring

print hash_func(bitstring("<+->"))
```


__Find an input string consisting only of the characters `"+-><; "` that produces
the hash value 0.__


Use the following program as basis: it builds a formula to analize another
simpler "hash funcion":

```python
def hash_func(inputstr):
    hash = 446055857
    for bit in inputstr:
        if int(bit) == 1:
            hash = (hash + 1364396257) & 0xffffffff
        else:
            hash = (hash * 3084817850) & 0xffffffff
    return hash
```

We can then use the following program to find preimages:

```python
#task_4.py
from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    input_bits = 8*10 #10 bytes of input
    input = b.Var(input_bits, "input")
    hash  = b.Const(446055857, 32)

    for i in range (0,input_bits):
      hashnew = b.Var(32,"hash"+str(i))
      # hash = if inptu[i]  then hash+136... else hash*308.. end
      b.Assert( hashnew == b.Cond(input[input_bits-i-1], hash + 1364396257, hash*3084817850  ) )
      hash = hashnew

    for i in range(0,input_bits/8):
      o = i * 8
      #all input bytes are from A..Z
      cur = b.Slice(input,o+7, o)
      b.Assert( cur >= 65)
      b.Assert( cur <= 90)

    b.Assert( hash == 2870426180)
    #import pdb; pdb.set_trace()
    res = b.Sat()
    if res == b.SAT:
        b.Print_model()
        print("{} {:x}".format(input.symbol, int(input.assignment,2)))
    else: 
        print("unsat")
```

Hint: you can create additional variables that do not influence the
satisfiability, but that will be printed by `Print_model()` to help you
debugging your formula.
