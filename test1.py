import os
import time
PI_PATH = 'E:\\Project\\Script\\P\\PY_Test\\'
os.chdir(PI_PATH)
import Lib1
from Lib1 import txt
from Lib1 import Auto_PI_main
fo = open( PI_PATH+"Auto_PI.txt",'r')
n = 0
PG_state = 0
Lcap = list()
Lpart = list()
Net_input = ''
fl = txt("Auto_PI.log","#Auto_PI.log",PI_PATH)
fl.writelines('Time: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n' )
for line in fo.readlines():
    n = n + 1
    if (line == "<Caps>\n") & (PG_state == 0):
        PG_state = 1
        fl.writelines("Adjustment capcitors' partname List:\n")
    elif (line == "<Ref>\n") & (PG_state == 1):
        PG_state = 2
        fl.writelines("Type of the adjsutment capcitors:"+str(len(Lcap))+'\n')
        fl.writelines("Adjustment capcitors' ref List:\n")
    elif (line == "<Netlist>\n") & (PG_state == 2):
        PG_state = 3
        fl.writelines("Number of the adjsutment ref:"+str(len(Lpart))+'\n')
    elif line == "<End>":
        PG_state = -1
        if Auto_PI_main(Lcap,Lpart,Net_input):
            print("Successful execution !\nConfigure file lines:",n)
        else:
            print("Failfure execution !\nConfigure file lines:",n)
    elif PG_state == 1:
        Lcap.append(line)
        fl.writelines(line)
    elif PG_state == 2:
        Lpart.append(line)
        fl.writelines(line)
    elif PG_state == 3:
        Net_input = line
        fl.writelines("Input the net name:" + Net_input + '\n')

fo.close()

