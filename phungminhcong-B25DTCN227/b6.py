a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

print("Cac so nguyen to trong khoang la:")

for number in range(a, b + 1):
    if number > 1:
        is_prime = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number)
