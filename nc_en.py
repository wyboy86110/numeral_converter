import sys

a = input("please input the number to convert")
b = input("please input the base of the number")
la=list (str(a))

for i in la:
    if int(i) > int(b):
        print ("the base and the number are not correspond")
        sys.exit()

c = input("please input the target base")
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
print ("the target number is：","".join(d))
