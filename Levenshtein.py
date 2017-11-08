#!/usr/bin/python3
seq1="*"+str(input("Bitte geben Sie Sequenz 1 ein: "))
seq2="+"+str(input("Bitte geben Sie Sequenz 2 ein: "))
normCost=input("Normale Kostenfunktion? [Y,n] ") or "y"
normCost=True if (normCost=="y") else False
GapCost=int(input("Gap-cost? [1]") or 1) if not normCost else 1
MissCost=int(input("Missmatch-Kosten? [1]") or 1) if not normCost else 1
MatchCost=int(input("Match-Kosten? [0]") or 0) if not normCost else 0
zeile=0
spalte=1
array = [[0 for x in range(len(seq2))] for y in range(len(seq1))]

def getMinimum(Array, zeile, spalte,matchCost):
 left=int(Array[zeile][spalte-1])+GapCost
 up=int(Array[zeile-1][spalte])+GapCost
 mMatch=int(Array[zeile-1][spalte-1])+matchCost
 return min([left,up,mMatch])

#Array vorbereiten
for i in range(len(seq1)):
 array[i][0]=i

for i in range(len(seq2)):
 array[0][i]=i

#Zeilenweise durchlaufen
for zeS in seq1[1:]:
 spalte=1
 zeile+=1
 for spS in seq2[1:]:
  array[zeile][spalte]=getMinimum(array,zeile,spalte,MatchCost if zeS==spS else MissCost)
  spalte+=1

levenshtein=array[zeile][spalte-1] #Letzten Wert holen
print (array)
print ("Levenshtein: ",levenshtein)
#Array sollte jetzt fertig sein
