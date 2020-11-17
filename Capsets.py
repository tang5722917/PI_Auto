import os
import sys
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
    def Is_cap_in_Netline(self,Line):
        for caps in self.capset:
            cap_l = str(caps[0])
            ref_l = str(caps[1])
            cap_l = cap_l.strip()
            ref_l = ref_l.strip()
            if cap_l in Line:
                return cap_l,ref_l
        return False

    def Generate_Netlsit(self,cPATH,f_netlsit):
        f = PI_Auto_Lib1.txt(str(self.Num)+"_Netlist.sp","*"+str(self.Num)+"_Netlist",cPATH)
        for Net_line in f_netlsit.readlines():
            Net_line = Net_line.strip()
            if len(Net_line) == 0:
                print(Net_line,file=f)
            elif Net_line[0] == '*':
                print(Net_line,file=f)
            elif "xmcap" not in Net_line :
                print(Net_line,file=f)
            elif Capsets.Is_cap_in_Netline(self,Net_line):
                temp = Capsets.Is_cap_in_Netline(self,Net_line)
                tempN = Net_line.find(temp[0],10)
                print("*"+Net_line,file=f)
                print(Net_line[0:tempN]+temp[0]+' '+temp[1],file=f)
            else:
                print(Net_line,file=f)
        f.close()
	
    def Generate_Bash(self,cPATH):
        str_bash = 'bs -os "RHEL6" -source /common/appl/dotfiles/hspice.CSHRC_2016.06-sp1 hspice '+str(self.Num)+'_Netlist.sp'+'| tee '+str(self.Num)+'_Netlist.log'
        print(str_bash)
        f = PI_Auto_Lib1.txt(str(self.Num)+"_Netlist.csh",str_bash,cPATH)
        f.close()
	
    def Perform_Bash(self,cPATH):
        Perform_str='csh '+cPATH+str(self.Num)+'_Netlist.csh'
        os.system(Perform_str)
	
    def Return_Peak(self,cPATH):
        PI_Fre = list()
        PI_Mag = list()
        Filename_log = cPATH+'SIM_Log/'+str(self.Num)+'_Netlist.log'
        fo_PIdata = open(Filename_log,'r')
        PI_data = PI_Auto_Lib1.Get_PIData(fo_PIdata)
        for data in PI_data:
            temp = str(data).split()
            PI_Fre.append(float(temp[0]))
            PI_Mag.append(float(temp[1]))
        Mag_Peak = max(PI_Mag)
        Fre_Peak = PI_Fre[PI_Mag.index(Mag_Peak)]
        fo_PIdata.close()
        return Fre_Peak,Mag_Peak
    
