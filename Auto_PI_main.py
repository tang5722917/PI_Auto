import os
from Capsets import Capsets
from PI_Auto import PI_Auto_Lib1
import itertools

def Auto_PI_main(Lcap,Lpart,Net_input,PATH,fl):
    capsets = list()
    capset = list()
    caps = list()
    NLc=len(Lcap)
    NLp=len(Lpart)
    captemp = list(itertools.product(Lcap,repeat=NLp))
    #完成capsets对象初始化
    for i in range(0,len(captemp)):
        for j in range(0,NLp):
            caps.append(Lpart[j])
            caps.append(captemp[i][j])
            capset.append(caps.copy())
            caps.clear()
        capsets.append(Capsets(capset.copy(),i))
        capset.clear()
    #生成capsets list
    PI_Auto_Lib1.mkdir(PATH+"Capset list")
    caplist_PATH = PATH+"Capset list//"
    os.chdir(caplist_PATH)
    print(PATH)
    for i in range(0,len(capsets)):
        print("Number of capset:",i)
        capsets[i].Generate_Capsetlsit(caplist_PATH)
    os.chdir(PATH)
    print("Successful generate capsets list !\n Number of capsets list",i+1,file=fl)
    #生成新的网表.sp文件
    PI_Auto_Lib1.mkdir(PATH+"Netlist")
    Netlist_PATH = PATH+"Netlist//"
    Net_f = open(Net_input.strip(),'r')
    os.chdir(Netlist_PATH)
    for i in range(0,len(capsets)):
        capsets[i].Generate_Netlsit(Netlist_PATH,Net_f)
        Net_f.seek(0)
    Net_f.close()
    print("Successful generate Netlist !\n Number of capsets list",i+1,file=fl)
    #生成.sp文件执行脚本
    for i in range(0,len(capsets)):
        capsets[i].Generate_Bash(Netlist_PATH)
    '''
    #执行.sp文件执行脚本
    for i in range(0,len(capsets)):
        capsets[i].Perform_Bash(Netlist_PATH)
    PI_Auto_Lib1.mkdir(PATH+"SIM_Wave")
    PI_Auto_Lib1.mkdir(PATH+"SIM_Log")
    os.system("mv *log ../SIM_Log")
    os.system("mv *ac0 ../SIM_Wave")
    os.system("mv *pa0 ../SIM_Wave")
    os.system("mv *ic0 ../SIM_Wave")
    os.system("mv *sc0 ../SIM_Wave")
    os.system("mv *st0 ../SIM_Wave")
    os.chdir(PATH)
    '''
    #处理结果数据
    PIresult_Fre = list()
    PIresult_Mag = list()
    print("Start deal PI date.",file=fl)
    for i in range(0,len(capsets)):
        PI_peak=capsets[i].Return_Peak(PATH)
        print("Netlsit"+str(i)+":"+"\nPeak Frequence:"+str(PI_peak[0])+"\nPeak Mag:"+str(PI_peak[1]),file=fl)
        PIresult_Fre.append(PI_peak[0])
        PIresult_Mag.append(PI_peak[1])
    Min_peak = min(PIresult_Mag)
    Min_Netlist = PIresult_Mag.index(Min_peak)
    Min_Peak_Fre = PIresult_Fre[Min_Netlist]
    print("Min peak Netlsit"+str(Min_Netlist)+":"+"\nMin Peak Frequence:"+str(Min_Peak_Fre )+"\nMin Peak Mag:"+str(Min_peak),file=fl)
    return True
