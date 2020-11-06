import os
from Capsets import Capsets;
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

def Auto_PI_main(Lcap,Lpart,Net_input):
    capsets = list()
    NLc=len(Lcap)
    NLp=len(Lpart)
    for i in 
    capsets.append(capset)
    set1 = Capsets(capsets)
    set1.print_capsets()
    return 1
