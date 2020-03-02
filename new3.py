print("i saw you ")
if __name__=="__main__":
    print("ok ")
class Num():
    def __init__(self,x):
        self.x=x
    def __str__(self):
        return "num : {}".format(self.x)
    def double(self):
        return "{}".format(self.x*2)

print(Num(1))
print(Num(1).double())