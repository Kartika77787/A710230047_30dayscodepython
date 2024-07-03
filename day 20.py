def celsius_to_fahrenheit(celsius):
    """
    Fungsi untuk mengkonversi suhu dari Celsius ke Fahrenheit.
    :param celsius: Suhu dalam Celsius
    :return: Suhu dalam Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Fungsi untuk mengkonversi suhu dari Fahrenheit ke Celsius.
    :param fahrenheit: Suhu dalam Fahrenheit
    :return: Suhu dalam Celsius
    """
    return (fahrenheit - 32) * 5/9

# Contoh penggunaan:
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}° Celsius = {fahrenheit}° Fahrenheit")

fahrenheit = 77
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}° Fahrenheit = {celsius}° Celsius")
