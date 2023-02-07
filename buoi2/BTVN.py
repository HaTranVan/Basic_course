salary_before = float(input('Nhap luong truoc thue: '))
age = int(input('Nhap tuoi: '))
married = input("Nhap tinh trang hon nhan: ") #1: đơn thân/ 2:đã lập gd / 3: đơn thân 
child = int(input('Nhap so con: '))

# a. Độc thân chịu thuế 5%, đã lập gia đình 3%, bố mẹ đơn thân 2%
if married == '1':
    thue = 0.05
elif married == '2':
    thue = 0.03
else:
    thue = 0.02
salary_after = thue * salary_before
print(f"Luong sau thue: {salary_after}")

# b. Có 1 con dc trừ thuế 3%, có 2 con được trừ 5%, từ con thứ 3
# được trừ 1% cho mỗi con

if child >= 3:
    thue = thue - 0.05 - 0.01 * (child - 2)
elif child == 2:
    thue -= 0.05
else:
    thue -= 0.03

salary_after_b = thue * salary_before 

#c.  Tiền lương trước thuế 10 triệu trở xuống được miễn thuế, trên 10
# triệu đến dưới 20 triệu chịu thuế 10%, từ 20 triệu trở lên chịu thuế
# lũy tiến 0.1% cho mỗi 1 triệu, nhưng tối đa ko vượt quá 5%
if salary_before > 20:
    thue = 0.1 + 0.001 * (salary_before - 20)
    if thue > 0.15:
        thue = 0.15
elif salary_before > 10:
    thue = 0.1
else:
    thue = 0
#d.  Độ tuổi từ 18-30 chịu thuế 6%, từ 31 đến 45 chịu thuế 9%, từ 46
# đến 60, với mỗi năm tuổi được giảm 0.1%, trên 60 tuổi được mức
# thuế cố định 4%
if age >= 18 and age >= 30:
    thue = 0.06
elif age >= 31 and age <= 45:
    thue = 0.9
elif age >= 46 and age <= 60:
    thue = 0.9 - 0.01 * (age - 45)
else:
    thue = 0.4
