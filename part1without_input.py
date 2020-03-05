from random import choice
from Bio.Seq import Seq

# define a function that generates a random sequence and put it into Bio.Seq object
def randomseq(l):
    sequence = ''
    while True:
        try:
            l = int(l or 1)
            break
        except ValueError:
            print("Oops! That was no valid number. Try again...")
    for i in range(int(l)):
        sequence += choice('ATCG')
        my_seq=Seq(sequence)
    return my_seq

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

