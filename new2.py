from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from random import choice
sequence1 = ''
sequence2 = ''
for i in range(100):
    sequence1 += choice('ATCG')
for i in range(100):
    sequence2 += choice('ATCG')
print(sequence1)
print(sequence2)
fasta1='First fasta file.fasta'
fasta2='Second fasta file.fasta'
with open(fasta1, 'w') as f:
    SeqIO.write(sequence1, f, "fasta")

