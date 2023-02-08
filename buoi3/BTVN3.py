with open(file="hoa/Iris.csv", mode="r") as file:
    a = file.readlines()

sum_width = [0, 0, 0] #loai 1, 2 , 3
sum_len = [0, 0, 0] #loai 1, 2 , 3
count = [0,0,0] #loai 1, 2 , 3

for line in a[1:]:
    text = line.split(',')
    if text[5] == 'Iris-setosa':
        count[0] +=1
        sum_len[0] += float(text[1])
        sum_width[0] += float(text[2])
    elif text[5] == 'Iris-virginica':
        count[1] +=1
        sum_len[1] += float(text[1])
        sum_width[1] += float(text[2])
    else:
        count[2] +=1
        sum_len[2] += float(text[1])
        sum_width[2] += float(text[2])
print(sum_len, sum_width, count, end='\n')