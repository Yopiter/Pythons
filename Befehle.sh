#Make Blast DB
zcat Chromosome.tar.gz | makeblastdb -in - -out dbName -dbtype nucl -title "DB Title" -parse_seqids

#Read Sequence from DB
blastdbcmd -db dbNAme -entry all -range 100-200

#Color Primer Seuquences
egrep -color '(Primer1|Primer2-Rev-Transkript)'

#Blast against remote nucleotide Database (blastp for proteins)
blastn -db nr -remote -query 'Sequence' -out ErgDatei.txt -html (-task blastn-short)
