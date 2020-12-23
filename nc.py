import sys

#a = input("请输入数字")
#b = input("请输入该数字的进制")
a= 11111
b = 2
la=list (str(a))

for i in la:
    if int(i) > int(b):
        print ("输入数字与进制不符")
        # sys.exit()

#c = input("请输入目标进制")
c = 8
j = 1
d1 = 0
#先转换成十进制
for i in la:
    if j <= len(la):
        d1 += int(i)*int(b)**(len(la)-j)
        j += 1
print (d1)
d2 = list (str(d1))
d = []
#把十进制数转换为目标进制
for i in range(10):
    if d1//(c**i) != 0:
        w1 = d1%(c**(i+1))
        d.insert(0,str(w1))
print ("该进制下数字为：","".join(d))