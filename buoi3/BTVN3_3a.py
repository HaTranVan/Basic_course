with open(file='D:/Khoa_CB/Code/buoi3/Iris_file.csv', mode="r") as file:
    a = file.readlines()

x = float(input("Nhap chieu dai: "))
y = float(input("Nhap chieu rong: "))

def count_dis(a,b,c,d):
    return ((a - c)**2 + (b - d)**2)**0.5

# a
type = ''
distance = []
for line in a[1:]:
    text = line.split(',')
    distance.append([count_dis(x,y,float(text[1]),float(text[2])), text[5]])

distance.sort(reverse=True)
# print(distance[0][1])

# b
sum_dis = [0,0,0] #tong khoang cach
count = [0,0,0] #dem so bong hoa
for line in a[1:]:
    text = line.split(',')
    if text[5] == 'Iris-setosa\n':
        sum_dis[0] += count_dis(x,y,float(text[1]),float(text[2]))
        count[0] += 1
    if text[5] == 'Iris-virginica\n':
        sum_dis[1] += count_dis(x,y,float(text[1]),float(text[2]))
        count[1] += 1
    if text[5] == 'Iris-versicolor\n':
        sum_dis[2] += count_dis(x,y,float(text[1]),float(text[2]))
        count[2] += 1
avg_dis = [[sum_dis[0]/count[0], 0],
           [sum_dis[1]/count[1], 1],
           [sum_dis[2]/count[2], 2]]
avg_dis.sort(reverse=True)
print('Loai hoa', avg_dis[0][1])


