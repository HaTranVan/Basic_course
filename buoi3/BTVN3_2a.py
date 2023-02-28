with open(file='D:/Khoa_CB/Code/buoi3/Iris_file.csv', mode="r") as file:
    a = file.readlines()

flower0 = []
flower1 = []
flower2 = []

for line in a[1:]:
    text = line.split(',')
    if text[5] == 'Iris-setosa\n':
        flower0.append([float(text[1]), float(text[2])])
    if text[5] == 'Iris-virginica\n':
        flower1.append([float(text[1]), float(text[2])])
    if text[5] == 'Iris-versicolor\n':
        flower2.append([float(text[1]), float(text[2])])
def max_len(list):
    list.sort(key= lambda x: x[1])
    return list[-1][0]
def max_width(list):
    list.sort(key= lambda x: x[1])
    return list[-1][1]

print(max_len(flower0), max_len(flower1), max_len(flower2))
print(max_width(flower0), max_width(flower1), max_width(flower2))
