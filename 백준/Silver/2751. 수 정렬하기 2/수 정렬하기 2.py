import sys
N = sys.stdin.readline()
A = list(map(int,sys.stdin.read().split()))

A.sort()
A = map(str, A)
sys.stdout.write("\n".join(A))
