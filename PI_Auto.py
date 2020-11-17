import os
import time
#当前目录地址 pwd
#PI_PATH = '/design02/DDR_SIM/V3MSLT_PI/PI_Test/PI_Test1/Test/'
PI_PATH = 'E:\\Project\\Script\\P\\PY_Test\\'
os.chdir(PI_PATH)
print(os.path.abspath('PI_Auto.py'))
from PI_Auto import PI_Auto_Lib1
import Auto_PI_main

fo = open( PI_PATH+"Auto_PI.txt",'r')
PG_state = 0
Lcap = list()
Lpart = list()
Net_input = ''
n = 0
fl = PI_Auto_Lib1.txt("Auto_PI.log","#Auto_PI.log",PI_PATH)
print('Time: '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n',file=fl)
for line in fo.readlines():
    n = n + 1
    if (line == "<Caps>\n") & (PG_state == 0):
        PG_state = 1
        print("Adjustment capcitors' partname List:\n",file=fl)
    elif (line == "<Ref>\n") & (PG_state == 1):
        PG_state = 2
        print("Type of the adjsutment capcitors:"+str(len(Lcap))+'\n',file=fl)
        print("Adjustment capcitors' ref List:\n",file=fl)
    elif (line == "<Netlist>\n") & (PG_state == 2):
        PG_state = 3
        print("Number of the adjsutment ref:"+str(len(Lpart))+'\n',file=fl)
    elif line == "<End>":
        PG_state = -1
        if Auto_PI_main.Auto_PI_main(Lcap,Lpart,Net_input,PI_PATH,fl):
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
        print("Input the net name:" + Net_input + '\n',file=fl)
fl.close()
fo.close()

