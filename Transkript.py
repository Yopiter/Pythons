#!/usr/bin/python3
seq=input(Sequenz bitte: ")
out=""
str_in=["A","C","G","T"]
str_out=["T","G","C",A"]
for s in seq:
 out+=str_out[str_in.index(s)]
print("Transkript: "+out)
print("Reverser Transkript: "+out[::-1])
