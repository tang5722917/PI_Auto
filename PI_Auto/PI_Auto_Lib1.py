import os
import os.path

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

def Get_PIData(fo):
    Status = False
    PI_data = list()
    Is_PIdata_str = "ac analysis tnom"
    for line in fo.readlines():
        if (((Is_PIdata_str in line) == True) and (Status == False)):
            Status = True
        elif ((Status == True) and (('y' in line) == True)):
            Status = False
        elif Status:
            PI_data.append(line.strip())
        else:
            continue
    PI_data = PI_data[4:]
    return PI_data

def Is_Netlist_No_execute(PATH,Filename):
    if os.path.isfile(PATH+"Netlist//"+Filename+".ac0"):
        return False
    elif os.path.isfile(PATH+"SIM_Wave//"+Filename+".ac0"):
        return False
    else:return True

def Deal_caplist(caplist,add_caplist):
    new_list = list()
    new_cap1 = list()
    new_cap2 = list()
    N_cap = len(caplist)
    N_add = len(add_caplist)
    for i in range(0,N_cap):
        for k in range(0,len(caplist[i])):
            new_cap1.append(caplist[i][k])
        for j in  range(0,N_add):
            new_cap2 = new_cap1.copy()
            for k in range(0,len(add_caplist[j])):
                new_cap2.append(add_caplist[j][k])
            new_list.append(new_cap2.copy())
            new_cap2.clear
        new_cap1.clear()
    return new_list

    

