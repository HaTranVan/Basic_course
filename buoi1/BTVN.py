#toa do diem H
x = float(input())
y = float(input())  

a = ((x-1)**2 + (y-2)**2)**0.5
b = ((x-3)**2 + (y-1)**2)**0.5
c = ((x-2)**2 + (y-3)**2)**0.5
d = ((x-5)**2 + (y-7)**2)**0.5
e = ((x-8)**2 + (y-5)**2)**0.5
f = ((x-7)**2 + (y-6)**2)**0.5

#a
kc = [a, b, c, d, e, f]
min_kc = a
for i in kc:
    if i < min_kc:
        min_kc = i
if min_kc == a or min_kc == b or min_kc == c:
    print('H thuoc class 1')
else:
    print('H thuoc class 2')
    
#b
if (a+b+c)/3 < (d+e+f)/3:
    print('H thuộc class 1 ')
else:
    print('H thuoc class 2')
    