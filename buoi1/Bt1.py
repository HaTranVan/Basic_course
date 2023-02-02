# nhập vao 3 so, so1 : tien gửi (triệu đồng) , số2 là lãi suất (lãi suất), số3 là kì hạn (năm)
# tính số tiền khi đến cuối kì hạn 

a = int(input('Nhap so tien gui: '))
b = float(input('Nhap lai suat: '))
c = int(input('Nhap ki han: '))

tien_nhan =  a*(1+b/1200)**(c*12)
print(tien_nhan)

print(type(True))