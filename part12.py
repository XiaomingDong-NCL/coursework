from random import choice
from Bio.Seq import Seq

# take input number as the length of the random sequence
# make sure the user enters an integer number

while True:
    try:
        x = int(input("Please enter a random integer number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

# generate a random sequence and put it in Bio.Seq object
sequence = ''
for i in range(int(x)):
    sequence += choice('ATCG')
    my_seq=Seq(sequence)

# define a new class My_randomseq, taking the random sequence as input
# reverse& complement classmethod，named rev_c(), taking the random sequence parameter
# protein classmethod，named protein(), taking the random sequence parameter generating three possible proteins

class My_randomseq():

    def __init__(self, x):
        self.x = x

    @classmethod
    def rev_c(cls,x):
        r_c=x.reverse_complement()
        return  cls(r_c)

    @classmethod
    def protein(cls, x):
        aa1 = ''
        aa2 = ''
        aa3 = ''
        protein=[]
        if len(x) % 3 == 0:
            aa1 = x.translate()
            aa2 = x[1:-2].translate()
            aa3 = x[2:-1].translate()
        elif (len(x) - 1) % 3 == 0:
            aa1 = x[:-1].translate()
            aa2 = x[1:].translate()
            aa3 = x[2:-2].translate()
        elif (len(x) - 2) % 3 == 0:
            aa1 = x[:-2].translate()
            aa2 = x[1:-1].translate()
            aa3 = x[2:].translate()
        protein.append(aa1)
        protein.append(aa2)
        protein.append(aa3)
        return cls(protein)

    def __str__(self):
        return "{}".format(self.x)

m=My_randomseq(my_seq)
r=My_randomseq.rev_c(my_seq)
p=My_randomseq.protein(my_seq)

# generate 2 random sequence with length 100
sequence1 = ''
sequence2 = ''
for i in range(100):
    sequence1 += choice('ATCG')
for i in range(100):
    sequence2 += choice('ATCG')
# define a function that finds the longest shared motif, taking two arguments, sequence1 & sequence2
# return the longest shared motif
def find_lmotif(s1,s2):
    s = [[0]*(1+len(s2)) for i in range (1+len(s1))]
    longest, x_longest = 0,0
    for x in range (1, 1+len(s1)):
        for y in range (1, 1+len(s2)):
            if s1[x-1] == s2[y-1]:
                s[x][y] = s[x-1][y-1]+1
                if s[x][y] > longest:
                    longest = s[x][y]
                    x_longest = x
            else:
                s[x][y] = 0
    return s1[x_longest-longest : x_longest]

l=find_lmotif(sequence1,sequence2)









