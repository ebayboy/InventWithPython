# -*- coding: UTF-8 -*-
filename = r"D:\source\InventWithPython\demo\rose1\usbPerf_itl_generic_64_smp_Dynamic_DI_28614.ini"
f = open(filename, "r+")
dics = {}
mode = 0

while 1:
    line = f.readline().strip()
    if not line:
        break

    if (line[0] == '['):
        # next status parse
        if (line.find('TestCase_') > 0):
            mode = 2
        else:
            mode = 1

    if (mode == 1):
        line = f.readline().strip()
        (key, value) = line.split('=', 2)
        dics[key]=value
    elif (mode==2):
        tempDic={}
        tempKey = line[1:len(line)-1]
        while 1:
            line = f.readline().strip()
            if not line:
                dics[tempKey] = tempDic
                break
            (key, value) = line.split('=', 2)
            tempDic[key]=value
        #read 
    mode = 0

print(dics)

# 关闭文件
f.close()

