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
    file.write(text)        #写入内容信息
    file.close()
    print ('ok')