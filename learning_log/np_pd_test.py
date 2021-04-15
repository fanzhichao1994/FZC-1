import pandas as pd
import numpy as np
s = pd.Series([1,2,5,5,np.nan,24])
s_1= pd.date_range('20210301',periods=6)
df = pd.DataFrame(np.random.rand(6,4),index=s_1,columns=list('ABCD'))
s_2 = pd.Series([4,7,-5,3],['d','b','a','c'])
print(s_2)
print(s_2.index)
print(s_2*2)
print(np.exp(s_2))
if "b" in s_2:
    print("the anwser is rigt")
if "f" not in s_2:
    print ("that's right")
dict_t1={"fanzhi":22,"fansifsa":24,"yinjgms":59}
index=["fanzhi","fansifsa","yinjgms","yinjgms22"]
s_3=pd.Series(dict_t1)
print(s_3)
s_4=pd.Series(dict_t1,index)
print(s_4)
print(pd.isnull(s_4))
print(np.arange(9).reshape(3,3))

s_5=pd.DataFrame(np.arange(16).reshape(4,4),index=['a','b','c','d'],columns=['one','two','three','four'])
print(s_5)
s_5.drop(['a','b'])
print(s_5.drop(['a','b']))
# print(df.index)
# print(df.values)
# print("=================")
# print(df)
# print("=================")
# print(s_1)
# print("=================")
# print(s)