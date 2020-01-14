rose:
不行，我得把这个文件里的每个case数据都取出来放到一个list里，之后跟另外一个文件的对应的case数据做对比呢

rose:
我是想着把文件头：[bsp]
bsp=itl_generic
[mp]
mp=smp
[bits]
bits=64
[tool]
tool=llvm

rose:
放一个字典里

rose:
把一个个case放字典里，再把所有case放到列表里

rose:
之后再把文件头的字典和case的列表放到列表里

rose:
因为会有多个文件

rose:
这是我的思路

rose:
后面再从列表和字典里读出来数据对比完放到新的字典和列表里，然后写到html里

rose:
不知道我是不是想得太复杂了