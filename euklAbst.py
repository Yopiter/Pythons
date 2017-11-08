#!/usr/bin/python3
import math
def getEuklAbstand():
 x1=float(input('x1'))
 y1=float(input('y1'))
 x2=float(input('x2'))
 y2=float(input('y2'))
 
 k1=(x1-y1)**2
 k2=(x2-y2)**2
 return(math.sqrt(k1+k2))

print('Euklidischer Abstand importiert')
