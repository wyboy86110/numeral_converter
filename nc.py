import sys

a = input("请输入数字")
b = input("请输入该数字的进制")
la=list (str(a))

for i in la:
    if int(i) > int(b):
        print ("输入数字与进制不符")
        sys.exit()

c = input("请输入目标进制")
j = 1
d1 = 0
#先转换成十进制
for i in la:
    if j <= len(la):
        d1 += int(i)*int(b)**(len(la)-j)
        j += 1
d2 = list (str(d1))
d = []
qz = d1
#把十进制数转换为目标进制
for i in range(10):
    if qz//int(c) >0:
        qy = qz%int(c)
        qz = qz//int(c)   
        d.insert(0,str(qy))
        if qz < int(c):
            d.insert(0,str(qz))
print ("该进制下数字为：","".join(d))
