#!/usr/bin/python3

def rekKoeff(n,k):
 assert 0<=k and k<=n
 if n==k or k==0:
  return 1
 else:
  return rekKoeff(n-1,k-1)+rekKoeff(n-1,k)

def getPascDreieck(maxN):
 gesList=[[1,0]]
 for n in range(1, maxN+1):
  row=[1]
  for spalte in range(1,n+1):
   wert=gesList[n-1][spalte-1]+gesList[n-1][spalte]
   row.append(wert)
  gesList+=[row+[0]]
 return gesList

def printDreieck(listDreieck):
 for row in listDreieck:
  print(row[:-1]) #Polster-Nullen am Ende der Zeilen wieder entfernen

n=int(input("n?\n"))
k=int(input("k?\n"))
rek=input("rekursiv? [Y,n]") or "y"
assert 0<=k and 0<n and k<=n
Output="("+str(n)+" "+str(k)+") = "
if(rek=="y" or rek=="Y"):
 Output+=str(rekKoeff(n,k))
else:
 listGes=getPascDreieck(n)
 printDreieck(listGes)
 Output+=str(listGes[n][k])
print(Output)
