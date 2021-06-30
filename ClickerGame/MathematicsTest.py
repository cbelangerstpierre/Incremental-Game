output = str()

num = 4
output += "Header,\n"
output += str(num) + ",\n"
for i in range(111):
    num *= 1.1
    new_num = "{:.2f}".format(num)
    output += str(new_num)
    output += ",\n"


print(output)
