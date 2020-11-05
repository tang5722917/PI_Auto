import os
PI_PATH = 'E:\\Project\\Script\\P\\PY_Test\\'
os.chdir(PI_PATH)
import Lib1
from Lib1 import txt
fo = open( PI_PATH+"Auto_PI.txt",'r')
#fw = 
n = 0
PG_state = 0
Lcap = list()
Lpart = list()
txt("Auto_PI.log","#Auto_PI.log",PI_PATH)
for line in fo.readlines():
    n = n + 1
    if (line == "<Caps>\n") & (PG_state == 0):
        PG_state = 1
        print("Start Read the list of capacitors")
    elif (line == "<Ref>\n") & (PG_state == 1):
        PG_state = 2
        print("Type of the adjsutment capcitors:",len(Lcap))
    elif (line == "<Net_name>\n") & (PG_state == 2):
        PG_state = 3
        print("Number of the adjsutment ref:",len(Lpart))
    elif PG_state == 1:
        Lcap.append(line)
    elif PG_state == 2:
        Lpart.append(line)
    elif line == "<End>":
        PG_state = -1
        print("End Program\nConfigure file lines:",n)
for cap in Lcap:
    print(cap)
for part in Lpart:
    print(part)
fo.close()

