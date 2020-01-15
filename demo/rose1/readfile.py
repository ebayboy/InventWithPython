#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

#filename = sys.argv[1]
filename = r"D:\source\InventWithPython\demo\rose1\usbPerf_itl_generic_64_smp_Dynamic_DI_28614.ini"

f = open(filename, "r+")
dics = {}
mode = 0

while 1:
	line = f.readline()
	if not line:
		break;
	line = line.strip()
	if not line:
		continue

	if (line[0] == '['):
		# next status parse
		if (line.find('TestCase_') > 0):
			mode = 2
		else:
			mode = 1

	if (mode == 1):
		line = f.readline()
		if not line:
			break
		line = line.strip()
		if not line:
			continue;

		(key, value) = line.split('=', 2)
		dics[key]=value
	elif (mode==2):
		tempDic={}
		tempKey = line[1:len(line)-1]
		i = 0
		while(1):
			line = f.readline()
			if not line:
				break;
			line = line.strip()
			if not line:
				continue

			if i == 4:
				dics[tempKey] = tempDic
				break
			(key, value) = line.split('=', 2)
			tempDic[key]=value
			i = i + 1
	mode = 0

print(dics)

f.close()




