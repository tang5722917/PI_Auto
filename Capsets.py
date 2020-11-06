class Capsets(object):
    def __init__(self, capset):
        self.capset = capset

    def __str__(self):
        return '(%s,%s)' %(self.capset)

    def print_capsets(self):
        for capset in self.capset:
            print("Ref:",capset[0],"Partnumber:",capset[1])