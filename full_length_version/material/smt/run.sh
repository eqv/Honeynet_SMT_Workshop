clang -c -g -emit-llvm -I./llbmc/examples $1 -o run.bc
#./llbmc/bin/llbmc -counterexample -memcpy=unroll -max-loop-iterations=10 -max-function-call-depth=5 --no-max-loop-iterations-checks run.bc
./llbmc/bin/llbmc -memcpy=unroll -max-loop-iterations=10 -max-function-call-depth=5 --no-max-loop-iterations-checks run.bc
