with open(file='D:/Khoa_CB/Code/buoi3/Iris_file.csv', mode="r") as file:
    a = file.readlines()

sum_width = [0, 0, 0] #loai 1, 2 , 3
sum_len = [0, 0, 0] #loai 1, 2 , 3
count = [0,0,0] #loai 1, 2 , 3

for line in a[1:]:
    text = line.split(',')
    if text[5] == 'Iris-setosa\n':
        count[0] +=1
        sum_len[0] += float(text[1])
        sum_width[0] += float(text[2])
    elif text[5] == 'Iris-versicolor\n':
        count[1] +=1
        sum_len[1] += float(text[1])
        sum_width[1] += float(text[2])
    else:
        count[2] +=1
        sum_len[2] += float(text[1])
        sum_width[2] += float(text[2])
print('Trung binh cong chieu dai loai 1,2,3:', 
round(sum_len[0]/count[0],2), round(sum_len[1]/count[1],2), round(sum_len[2]/count[2],2))


# -------------Cach 2 ---------------#
# x = {}
# cd = {}
# cr = {}
# list = []
# for line in a[1:]:
#     list.append(line.split(','))
# for i in list:
#     if i[5] in x:
#         x[i[5]] += 1
#         cd[i[5]] += float(i[1])
#         cr[i[5]] += float(i[2])
#     else:
#         x[i[5]] = 1
#         cd[i[5]] = float(i[1])
#         cr[i[5]] = float(i[2])
# print(x, cd, cr)