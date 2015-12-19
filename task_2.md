We are interested in some strange behaviour regarding integer overflows.
Assume you want to find out if there is an 64 bit integer 
`x < 0` such that `x * 133713378 == 1337`.


__Adapt the the following program (`task_2.py`) to answer your question:__

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

An api reference can be found here: (http://fmv.jku.at/boolector/doc/pyboolector.html).
