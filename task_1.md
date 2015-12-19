Install boolector and the python api. To do so perform the following steps:

```
wget 'http://fmv.jku.at/boolector/boolector-2.2.0-with-lingeling-bal.tar.bz2'
tar -xf boolector-2.2.0-with-lingeling-bal.tar.bz2
cd boolector-2.2.0-with-lingeling-bal
cd lingeling
./configure.sh -fPIC # we need Position independend code for the python wrapper
make
cd ..
cd boolector
./configure -python #add python bindings
make
sudo cp boolector /usr/bin/
sudo python setup.py install
```

Then you should be able to run the following python script successfully which
should print 'x 5'. It asks the smt solver to find an 64 bit integer x such
that `x*20 == 100 and x < 100` (with an unsigned interpretation of x). Thus
there is exactly one solution.

```python
from boolector import Boolector

if __name__ == "__main__":
    b = Boolector() 
    b.Set_opt("model_gen", 1)

    const   = b.Const(100, 64)
    x       = b.Var(64, "x")


    b.Assert(x * 20 == 100)
    b.Assert(b.Ult(x, 100))

    res = b.Sat()
    if res == b.SAT:
        #b.Print_model()
        print("{} {}".format(x.symbol, int(x.assignment,2)))
        #import pdb; pdb.set_trace()
    else: 
        print("unsat")
```

Then go (http://llbmc.org/downloads.html), register with some email and obtain a
copy of llbmc.
