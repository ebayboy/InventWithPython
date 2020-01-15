
dic1 = {'key1': 'value1', 'key2': 'value2', 'key3': "3333"}
dic2 = {'key2': 'vlaue2', 'key3': 444}

for key in dic1:
    print("key:", key)
    print("dic1_value:", dic1[key])
    # 在字典2中查找字典的key是否存在
    for key2 in dic2:
            # key比较
        if key == key2:
            print("==================EQUAL=============")
            print("%s=%s" % (key, key2))
            print("value:%s value2:%s" % (dic1[key], dic2[key2]))
            print(type(dic1[key]))
            print(type(dic2[key]))
            # 判断类型是str， 转换成数字
            if (type(dic1[key]) == str and dic1[key].isnumeric()):
                print("number1:", int(dic1[key]))
            print("==================EQUAL END=============")
