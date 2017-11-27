#! /usr/bin/python3

def iterativ(n):
 if(n<=0):
  return 0
 elif(n==1):
  return 1
 i0=0
 i1=1
 i=0
 for counter in range(n-1):
  i=i0+i1
  i0=i1
  i1=i
 return i

n=int(input("Anzahl? "))
for l in range(n+1):
 print("F("+str(l)+"):",iterativ(l))
