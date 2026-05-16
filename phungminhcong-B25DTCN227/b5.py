n = int(input("Nhap mot so nguyen duong: "))
giai_thua = 1

for i in range(1, n + 1):
    giai_thua *= i

print("Giai thua cua", n, "la:", giai_thua)
