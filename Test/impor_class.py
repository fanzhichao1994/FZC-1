# 导入模块类联系
from Test import Human
from collections import OrderedDict

man = Human("fanzhihao", 26, "black")
man.get_named()
print(man.get_named())

favorite_languages = OrderedDict()
favorite_languages["hen"] = "python"
favorite_languages["sarah"] = "c"
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is" + language.title() + ".")
# 打开txt格式的文件，并读取打印
with open("pi_dilith.txt")as file_object:
    contents = file_object.read()
    # 字符串的rstrip方法去除末尾空行
    print(contents.rstrip())



