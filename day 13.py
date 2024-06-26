# Menggunakan for loop untuk iterasi dalam list
fruits = ["apple", "banana", "cherry"]
print("For loop dengan list:")
for fruit in fruits:
    print(fruit)
print()  # Tambahkan baris kosong untuk memisahkan output

# Menggunakan while loop untuk iterasi selama kondisi benar
count = 0
print("While loop dengan kondisi:")
while count < 5:
    print("Count is:", count)
    count += 1
print()  # Tambahkan baris kosong untuk memisahkan output

# Menggunakan range dalam for loop
print("For loop dengan range:")
for i in range(5):
    print(i)
print()  # Tambahkan baris kosong untuk memisahkan output

# Menggunakan break dan continue dalam loop
print("For loop dengan break dan continue:")
for i in range(10):
    if i == 5:
        break  # Menghentikan loop ketika i sama dengan 5
    if i % 2 == 0:
        continue  # Melanjutkan ke iterasi berikutnya jika i adalah angka genap
    print(i)
print()  # Tambahkan baris kosong untuk memisahkan output

# Nested loop
print("Nested loop:")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
print()  # Tambahkan baris kosong untuk memisahkan output
