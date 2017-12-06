#!/usr/bin/python3
def doSequenceStatistiks(line):
 global anzahl_ges
 for AA in line:
  if AA in 'ACDEFGHIKLMNPQRSTVWY':
   vorkommen=statistik[AA] if AA in statistik else 0
   vorkommen+=1
   statistik[AA]=vorkommen
   anzahl_ges+=1


filename=input('Filename? [seq.txt]\n')or 'seq.txt'
pdb=open(filename)
statistik={}
anzahl_ges=0
protein=False
for line in pdb:
 line=line.strip()
 if line.startswith('>'):
  if 'mol:protein' in line:
   #Protein gefunden
   protein=True
  else:
   protein=False
 elif protein and not line.startswith(';') and line != '':
   #Sequenz bearbeiten
   doSequenceStatistiks(line)

#Auswertung
for AA in statistik.keys():
 print(AA, statistik[AA], str(round(int(statistik[AA])/anzahl_ges*100,2))+'%')
print(anzahl_ges,'Aminosäuren insgesamt')
pdb.close()
