from requests import get,put

ret=put('http://localhost:5000/todo1', data={'data':'data1'}).json()
print("put:")
print(ret)

ret=get('http://localhost:5000/todo1').json()
print("get:")
print(ret)


ret=put('http://localhost:5000/todo2', data={'data':'data2'}).json()
print("put2:")
print(ret)


ret=get('http://localhost:5000/todo2').json()
print("get2:")
print(ret)