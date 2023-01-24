#print("hello")

class Computer:
    def __init__(self):
        self.name="Bittu"
        self.age=23
        #print("without calling init")
    # def update(self):
    #     self.age=30
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
        #print("configurations of system",self.cpu,self.ram)

cm1=Computer()
cm2=Computer()
cm2.age=24
if cm1.compare(cm2):
    print("they are same")
else:
    print("They are different")
# cm2.ram=512
# cm2.cpu="i7"
# Computer.update(cm1)
#cm1.update()
#cm2.update()