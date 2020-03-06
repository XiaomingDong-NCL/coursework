from django.db import models
from part1without_input import My_randomseq, randomseq

# creat length models
class Integerlength(models.Model):
    integerlength = models.IntegerField()

