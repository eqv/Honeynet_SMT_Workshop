Assume you encountered some strange obfuscated code that uses the following :
`((x | y) & ~(x & y)) + 2*(x&y)`

running this for some values of `x` and `y` you assume that this is equivalent to
`x+y`. However you'd rather be sure. 
You can use SMT solvers not only to find satisfying solutions (such as in task
1) but also to show that there are no such solutions.  Assume you want to show
that `x+y == y+x`. 
The trick is to make the smt solver look for values `x`,`y` such that `x+y !=
y+x`.
If no such pair exist, we know that `x+y == y+x`. In general, we can prove that
some formula is always true by showing that the negation is always false. 

__Test if the formula above is equivalent to `x+y`.__

This can also be used to deobfuscated fake conditional jumps. Assume there is
some code such as

```C
if((x*x+x)%2 == 0){
//[....]
}else{
//[....]
}
```

__Can the else branch ever be taken? Use the trick above to find out!__
