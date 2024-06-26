class AkunEmail:
    def __init__(self, email, password):
        self.__email = email  # atribut private
        self.__password = password  # atribut private

    # Getter untuk email
    def get_email(self):
        return self.__email

    # Setter untuk email
    def set_email(self, email):
        if isinstance(email, str) and "@" in email:  # validasi email harus string dan mengandung '@'
            self.__email = email
        else:
            raise ValueError("Email tidak valid.")

    # Getter untuk password
    def get_password(self):
        return self.__password

    # Setter untuk password
    def set_password(self, password):
        if isinstance(password, str) and len(password) >= 6:  # validasi password harus string dan minimal 6 karakter
            self.__password = password
        else:
            raise ValueError("Password harus berupa string dan minimal 6 karakter.")

# Contoh penggunaan kelas AkunEmail
akun1 = AkunEmail("user@example.com", "password123")

# Mengakses data menggunakan getter
print(akun1.get_email())  # Output: user@example.com

# Mengubah data menggunakan setter
akun1.set_email("newuser@example.com")
akun1.set_password("newpassword456")

print(akun1.get_email())  # Output: newuser@example.com

# Contoh validasi setter
try:
    akun1.set_email("invalidemail")
except ValueError as e:
    print(e)  # Output: Email tidak valid.
