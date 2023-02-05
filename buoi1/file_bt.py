# point(x, y, class)
space = {
    "A": [1, 2, 1],
    "B": [3, 1, 1],
    "C": [2, 3, 1],
    "D": [5, 7, 2],
    "E": [8, 5, 2],
    "F": [7, 6, 2]
}

x = int(input("Nhap toa do x: "))
y = int(input("Nhap toa do y: "))
# Ha luu kq y a, Hb luu kq y b
Ha = [x, y, 0]
Hb = [x, y, 0]

# Ham tinh khoang cach
def distance(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2


min_dis = 99999
i = 1
avg_dis = 0
min_avg = 99999
for p in space:
    dis = distance(space[p], Ha)
    # Tinh toan y a
    if min_dis > dis:
        min_dis = dis
        Ha[2] = space[p][2]
    # Tinh toan y b
    avg_dis += dis
    if i % 3 == 0:
        avg_dis = avg_dis / 3
        if min_avg > avg_dis:
            min_avg = avg_dis
            Hb[2] = int(i / 3)
        avg_dis = 0
    i = i + 1

print(f"Class cua Ha la: class {Ha[2]}")
print(f"Class cua Hb la: class {Hb[2]}")

