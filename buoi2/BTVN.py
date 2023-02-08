salary_before = float(input('Nhap luong truoc thue: '))
age = int(input('Nhap tuoi: '))
married = input("Nhap tinh trang hon nhan: ") #1: đơn thân/ 2:đã lập gd / 3: đơn thân 
child = int(input('Nhap so con: '))

thue = 0
# a. Độc thân chịu thuế 5%, đã lập gia đình 3%, bố mẹ đơn thân 2%
if married == '1':
    thue = 5
elif married == '2':
    thue = 3
else:
    thue = 2

# b. Có 1 con dc trừ thuế 3%, có 2 con được trừ 5%, từ con thứ 3
# được trừ 1% cho mỗi con
if child == 1:
    thue -= 3
elif child == 2:
    thue -= 5
else:
    thue -= (5 + 1 * (child - 2))


#c.  Tiền lương trước thuế 10 triệu trở xuống được miễn thuế, trên 10
# triệu đến dưới 20 triệu chịu thuế 10%, từ 20 triệu trở lên chịu thuế
# lũy tiến 0.1% cho mỗi 1 triệu, nhưng tối đa ko vượt quá 5%
thue_c = 0
if salary_before <= 10 :
    thue_c = 0
elif salary_before > 10 and salary_before < 20:
    thue_c = 0.1
else:
    thue_c = 0.1 + (salary_before - 20) * 0.001
    if thue_c > 0.15:
        thue_c = 0.15
#d.  Độ tuổi từ 18-30 chịu thuế 6%, từ 31 đến 45 chịu thuế 9%, từ 46
# đến 60, với mỗi năm tuổi được giảm 0.1%, trên 60 tuổi được mức thuế cố định 4%
thue_d = 0
if age >= 18 and age <= 30:
    thue_d = 6
elif age >= 31 and age <= 45:
    thue_d = 9
elif age >= 46 and age <= 60:
    thue_d = 9 - (age - 45)*0.1
else:
    thue_d = 4

thue_all = thue + thue_c + thue_d
salary_after =salary_before - thue_all*salary_before