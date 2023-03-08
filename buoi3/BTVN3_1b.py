with open(file='D:/Khoa_CB/Code/buoi3/Iris_file.csv', mode="r") as file:
    a = file.readlines()

# flower0 = []
# flower1 = []
# flower2 = []
# for line in a[1:]:
#     text = line.split(',')
#     if text[5] == 'Iris-setosa\n':
#         flower0.append(float(text[1]))
#     if text[5] == 'Iris-virginica\n':
#         flower1.append(float(text[1]))
#     if text[5] == 'Iris-versicolor\n':
#         flower2.append(float(text[1]))

# def print_max_len(list):
#     list.sort(reverse=True)
#     for i in range(10):
#         print(list[i], end=' ')
# print_max_len(flower0)

flowers = []
for line in a[1:]:
    text = line.split(',')
    flower = []
    flower.append(text[1])
    flower.append(text[2])
    if text[5] == 'Iris-setosa\n':
        flower.append(0)
    if text[5] == 'Iris-versicolor\n':
        flower.append(1)
    if text[5] == 'Iris-virginica\n':
        flower.append(2)
    flowers.append(flower)

flowers.sort(reverse=True)
print(flowers)
for i in range(3):
    count_flower = 0
    if i == 0:
        print('Iris-setosa')
    elif i == 1:
        print('Iris-versicolor')
    else:
        print('Iris-virginica')
    for flower in flowers:
        if flower[2] == i:
            print(flower[0])
            count_flower += 1
        if count_flower == 10:
            break
