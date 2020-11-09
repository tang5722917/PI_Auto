import os
import itertools
from Capsets import Capsets

def mkdir(path):
	folder = os.path.exists(path)
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print ("---  new folder...  ---")
		print ("---  OK  ---")
	else:
		print ("---  There is this folder!  ---")
 
def txt(filename,text,PATH):              #定义函数名
    if not os.path.exists(PATH):     #判断当前路径是否存在，没有则创建new文件夹
        os.makedirs(PATH)
    file = open(filename,'w')
    file.truncate()         #如果已存在该文件，则清空文件内容
    file.write(text+'\n')        #写入内容信息
    print ('ok')
    return file

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
    mkdir(PATH+"Capset list")
    caplist_PATH = PATH+"Capset list//"
    os.chdir(caplist_PATH)
    print(PATH)
    for i in range(0,len(capsets)):
        print("Number of capset:",i)
        capsets[i].print_capsets()
        capsets[i].Generate_Capsetlsit(caplist_PATH)
    os.chdir(PATH)
    print("Successful generate capsets list !\n Number of capsets list",i+1,file=fl)
    #生成新的网表.sp文件

    return True
