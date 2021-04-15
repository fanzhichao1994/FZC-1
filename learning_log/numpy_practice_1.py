import numpy as np
import math
import  pandas as pd
# path = "Table.txt"
# code_list=[]
# with open(path) as file:
#     read_data=file.read()
# file.close()
# print(read_data)
# code_list=read_data
# print(code_list)
# print("=======code"+str(0)+"=========")
# print(code_list[:7])
# print(type(code_list[:7]))
#
#
#
#
# data = np.random.randn(2,3)
# arr = np.array([[1,2,3,4],[1,2,5,6]])
# arr_1 = np.array([[1,2,2,4],[1,3,4,6]])
# arr_2 = np.array([[[2,3,3,3],[2,2,2,2,],[3,3,3,3]]])
# # print(arr_2)
# # print(arr)
# # print(arr.dtype)
# # print(arr.shape)
# # print(arr**2)
# # print(arr>arr_1)
# # print(data)
# # print(data.dtype)
# # print(data.shape)
# arr_4 = arr_1.copy()
# arr_4=arr_1[:]
# arr_4[0][2]=25
# print(arr_4)
# print(arr_1)
#
# arr_5 = np.empty((8,4))
# for i  in  range(8):
#     arr_5[i] = i
# print(arr_5)
# print(arr_5[[6,7,2,1]])
# arr = np.arange(32).reshape(8,4)
# print(arr)
# print(arr[[1,2,2,1],[2,2,1,1]])
# print(arr.T)
# arr2=np.random.randn(5)
# print(arr2)
# arr3 = np.arange(20).reshape(2,10)
# print(arr3)
#
# x=np.array([[1,2,3,4],[2,3,4,5]])
# print(x.shape)
# math.log()
obj = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(obj)
obj2 = pd.DataFrame(np.arange(15).reshape(5,3),index=['a','b','c','d','e'],columns=['m','n','h'])
print(obj2)
state = ['fan','zhi','chao','sj','saf']
obj3=obj2.reindex(['fan','zhi','chao','sj','saf'])
obj4 = obj2.reindex(columns=state)
col = ['m','n']
li = ['a','b','c']
print(obj3)
print(obj4)
print(obj2.loc[['a','b','c'],col])
ob6 = obj2.drop('c')
print(ob6)
print(obj2)
obj2.drop('m',axis=1,inplace=True)
print("===========^^^================")
print(obj2)
m = pd.Series([1,2,3,45,2,6,7],index=[0,1,2,3,4,5,6])
n =[1,2,3,45,2,6,7]
print(m)
print(m[:6])
print(n[:6])
print(obj2[:2])


