#! /usr/bin/python3

def iterativ(n):
 i0=0
 i1=1
 for counter in range(n-2):
  i=i0+i1
  i0=i1
  i1=i
 return i

n=int(input("Anzahl? "))
print(iterativ(n))
