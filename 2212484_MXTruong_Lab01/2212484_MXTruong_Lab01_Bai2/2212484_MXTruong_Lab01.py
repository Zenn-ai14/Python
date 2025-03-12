import math

# 1. Tính toán cơ bản
def ham_tinhab(a, b):
    print("1.1. a + b =", a + b)
    if b != 0:
        print("1.2. a / b =", a / b)
    else:
        print("Không thể chia cho 0.")
    print("1.3. a ^ b =", a ** b)
#a = float(input("Nhập giá trị a: "))
#b = float(input("Nhập giá trị b: "))
#ham_tinhab(a, b)

# 2. Tính diện tích hình tròn khi biết bán kính
def dientich_hinhtron(r):
    dt = math.pi * r ** 2
    print("2. Diện tích hình tròn khi biết bán kính R:", dt)
#r = float(input("Nhập bán kính hình tròn: "))
#dientich_hinhtron(r)

# 3. Xuất các số nguyên tố trong một khoảng
def so_nguyento(start, end):
    def is_sont(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    sont = [n for n in range(start, end + 1) if is_sont(n)]
    print("3. Các số nguyên tố trong khoảng:", sont)
#start = int(input("Nhập giá trị start: "))
#end = int(input("Nhập giá trị end: "))
#so_nguyento(start, end)

# 4. Kiểm tra số Fibonacci
def is_fibonacci(n):
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x
    return is_perfect_square(5 * n**2 + 4) or is_perfect_square(5 * n**2 - 4)
#n = int(input("Nhập một số nguyên n: "))
#print(f"4. {n} là số Fibonacci: {is_fibonacci(n)}")

# 5. Tìm số Fibonacci thứ n
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
#n = int(input("Nhập chỉ số n của dãy Fibonacci: "))
#print(f"5.1 Fibonacci thứ {n} (đệ quy): {fibonacci_recursive(n)}")
#print(f"5.2 Fibonacci thứ {n} (không đệ quy): {fibonacci_iterative(n)}")


# 6. Tính tổng n số Fibonacci đầu tiên
def sum_fibonacci_recursive(n):
    return sum(fibonacci_recursive(i) for i in range(n))
def sum_fibonacci_iterative(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    total = a + b
    for _ in range(2, n):
        a, b = b, a + b
        total += b
    return total
#n = int(input("Nhập số lượng n số Fibonacci:"))
#print("6.1 Tổng", n, "số Fibonacci (đệ quy):", sum_fibonacci_recursive(n))
#print("6.2 Tổng", n, "số Fibonacci (không đệ quy):", sum_fibonacci_iterative(n))

# 7. Tính tổng căn bậc 2 của n số nguyên đầu tiên
def sum_square_roots(n):
    total = sum(math.sqrt(i) for i in range(1, n + 1))
    print("7. Tổng căn bậc 2:", total)
#n= int(input("Nhập n số nguyên đầu tiên:"))
#sum_square_roots(n)

# 8. Giải phương trình bậc 2
def pt_bac2(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("8. Phương trình có hai nghiệm phân biệt:", x1, "và", x2)
#a = float(input("Nhập a: "))
#b = float(input("Nhập b: "))
#c = float(input("Nhập c: "))        
#pt_bac2(a, b, c)

# 9. Tính n! (giai thừa)
def ngiaithua_dequy(n):
    if n <= 1:
        return 1
    return n * ngiaithua_dequy(n - 1)
def ngiaithua_khongdequy(n):
    kq = 1
    for i in range(2, n + 1):
        kq *= i
    return kq
#n = int(input("Nhập n:"))
#print(f"9.1 {n}! (đệ quy):", ngiaithua_dequy(n))
#print(f"9.2 {n}! (không đệ quy):", ngiaithua_khongdequy(n))

# 10. In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
def sao_sao(n):
    for i in range(1, n + 1):
        print('*' * i)
#n = int(input("Nhập số hàng: "))
#sao_sao(n)

# 11.Đổi giờ - phút – giây
def doi_gio_phut_giay(soGiay):
    gio = soGiay // 3600         # Lấy số giờ (1 giờ = 3600 giây)
    soGiay = soGiay % 3600       # Lấy số giây còn lại sau khi tính giờ
    phut = soGiay // 60          # Lấy số phút (1 phút = 60 giây)
    giay = soGiay % 60           # Lấy số giây còn lại

    # In kết quả theo định dạng giờ:phút:giây
    print(f"{gio}:{phut}:{giay}")

# Nhập số giây từ người dùng
#soGiay = int(input("Nhập số giây: "))
#doi_gio_phut_giay(soGiay)

def main():
    while True:
        print("\n=== Menu ===")
        print("1. Tính toán cơ bản")
        print("2. Tính diện tích hình tròn")
        print("3. Xuất các số nguyên tố trong một khoảng")
        print("4. Kiểm tra số Fibonacci")
        print("5. Tìm số Fibonacci thứ n")
        print("6. Tính tổng n số Fibonacci đầu tiên")
        print("7. Tính tổng căn bậc 2 của n số nguyên đầu tiên")
        print("8. Giải phương trình bậc 2")
        print("9. Tính n! (giai thừa)")
        print("10.In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)")
        print("11.Đổi giờ - phút – giây")
        print("0. Thoát")
        choice = input("Chọn chức năng (0-12): ")
        if choice == "1":
            a = float(input("Nhập giá trị a: "))
            b = float(input("Nhập giá trị b: "))
            ham_tinhab(a, b)
        elif choice == "2":
            r = float(input("Nhập bán kính hình tròn: "))
            dientich_hinhtron(r)
        elif choice == "3":
            start = int(input("Nhập giá trị start: "))
            end = int(input("Nhập giá trị end: "))
            so_nguyento(start, end)
        elif choice == "4":
            n = int(input("Nhập một số nguyên n: "))
            print(f"{n} là số Fibonacci: {is_fibonacci(n)}")
        elif choice == "5":
            n = int(input("Nhập chỉ số n của dãy Fibonacci: "))
            print(f"Fibonacci thứ {n} (đệ quy): {fibonacci_recursive(n)}")
            print(f"Fibonacci thứ {n} (không đệ quy): {fibonacci_iterative(n)}")
        elif choice == "6":
            n = int(input("Nhập số lượng n số Fibonacci: "))
            print("Tổng", n, "số Fibonacci (đệ quy):", sum_fibonacci_recursive(n))
            print("Tổng", n, "số Fibonacci (không đệ quy):", sum_fibonacci_iterative(n))
        elif choice == "7":
            n = int(input("Nhập số lượng n số nguyên đầu tiên: "))
            sum_square_roots(n)
        elif choice == "8":
            a = float(input("Nhập a: "))
            b = float(input("Nhập b: "))
            c = float(input("Nhập c: "))
            pt_bac2(a, b, c)
        elif choice == "9":
            n = int(input("Nhập n: "))
            print(f"{n}! (đệ quy):", ngiaithua_dequy(n))
            print(f"{n}! (không đệ quy):", ngiaithua_khongdequy(n))
        elif choice == "10":
            n = int(input("Nhập số hàng: "))
            sao_sao(n)
        elif choice == "11":
            soGiay = int(input("Nhập số giây: "))
            doi_gio_phut_giay(soGiay)
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
main()








