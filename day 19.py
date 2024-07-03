# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x / y

# Main program
if __name__ == "__main__":
    print("Program Kalkulator Sederhana")

    while True:
        print("\nPilih Operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5): ")

        if choice == '5':
            print("Keluar dari program.")
            break

        num1 = float(input("Masukkan bilangan pertama: "))
        num2 = float(input("Masukkan bilangan kedua: "))

        if choice == '1':
            print(f"Hasil: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Hasil: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Hasil: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Hasil: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
