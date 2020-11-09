import os
from PI_Auto import PI_Auto_Lib1

class Capsets(object):
    def __init__(self, capset, Num):
        self.capset = capset
        self.Num = Num
    def __str__(self):
        return '(%s,%s)' %(self.capset)

    def print_capsets(self):
        for caps in self.capset:
            print(self.Num,": Ref:",caps[0],"Partnumber:",caps[1])

    def Generate_Capsetlsit(self,cPATH):
        f = PI_Auto_Lib1.txt(str(self.Num)+"_capset list.txt","#"+str(self.Num)+"_capset list",cPATH)
        for caps in self.capset:
            print(str(caps).replace('\\n', ''),file=f)
        f.close()
