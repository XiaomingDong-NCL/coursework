from django.db import models
from part1without_input import My_randomseq, randomseq

# creat length models ,set mat length 10,000
class Integerlength(models.Model):
    integerlength = models.IntegerField()
    length = integerlength
    myseq = randomseq(length)
    myseq_s = My_randomseq(myseq)
    myseq_rc = My_randomseq.rev_c(myseq)
    myseq_p = My_randomseq.protein(myseq)

