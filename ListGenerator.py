#!/usr/bin/python3
import random

def getListe(length):
 liste=[]
 for i in range(length):
  liste=liste+[(random.random()*100)]
 return liste

def getArMittel(liste):
 ges=0.0
 for i in liste:
  ges=ges+i
 return ges/len(liste)

def getGeoMittel(liste):
 ges=1.0
 for i in liste:
  ges=ges*i
 return ges**(1/len(liste))

length=int(input('Länge der Liste: '))
liste=getListe(length)
print('Liste:',liste)
print('Arithmetisches Mittel:', getArMittel(liste))
print('Geometrisches Mittel:', getGeoMittel(liste))

