file_name= "pi_dilith.txt"
with open(file_name)as file_object:
    lines=file_object.readline()
code=""
for line in lines:
    code=code+line.strip()
print(code)
print(len(code))
