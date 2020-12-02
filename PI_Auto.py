import os
import time
#当前目录地址 pwd
#PI_PATH = '/design02/DDR_SIM/V3MSLT_PI/PI_Test/PI_Test1/Test/'
#PI_PATH = 'E:\\Project\\Script\\PY\\PY_PI_V02\\'
PI_PATH = str(os.getcwd())
PI_PATH = PI_PATH + '/'
print(PI_PATH)
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
    if (line == "<Set_Num>\n") & (PG_state == 0):
        PG_state = 1
    elif (line == "<Set>\n") & (PG_state == 1):
        PG_state = 2
        capN = list()
        partN = list()
    elif (line == "<Caps>\n") & (PG_state == 2):
        PG_state = 3
        print("Adjustment capcitors' partname List:\n",file=fl)
    elif (line == "<Ref>\n") & (PG_state == 3):
        PG_state = 4
        print("Type of the adjsutment capcitors:"+str(len(capN))+'\n',file=fl)
        print("Adjustment capcitors' ref List:\n",file=fl)
    elif (line == "<Endset>\n") & (PG_state == 4):
        print("Number of the adjsutment ref:"+str(len(partN))+'\n',file=fl)
        PG_state = 1
        Lcap.append(capN.copy())
        Lpart.append(partN.copy())
        capN.clear()
        partN.clear()
    elif (line == "<Netlist>\n") & (PG_state == 1):
        PG_state = 5
    elif line == "<End>":
        PG_state = -1
        if Auto_PI_main.Auto_PI_main(Set_N,Lcap,Lpart,Net_input,PI_PATH,fl):
            print("Successful execution !\nConfigure file lines:",n)
        else:
            print("Failfure execution !\nConfigure file lines:",n)
    elif PG_state == 1:
        print(line)
        Set_N = int(line.strip())
        print("Number of the adjsutment sets:"+str(Set_N)+'\n',file=fl)
    elif PG_state == 3:
        capN.append(line)
        fl.writelines(line)
    elif PG_state == 4:
        partN.append(line)
        fl.writelines(line)
    elif PG_state == 5:
        Net_input = line
        print(Net_input)
        print("Input the net name:" + Net_input + '\n',file=fl)
    else:
        print("Error"+str(line),file=fl)
fl.close()
fo.close()

