"""
Program: Konversi Suhu dan Status Kondisi Ruangan
Praktikum Algoritma dan Pemrograman 1
Dibuat oleh: Annafi Al Ghifari (NIM: 2511533013)
"""

# Menampilkan Header Program
print("=" * 40)
print("   PROGRAM KONVERSI SUHU & MONITORING   ")
print("=" * 40)
print()

# Mengambil input nama dan nilai suhu Celcius
nama_operator = input("Masukkan Nama Operator : ")
celsius_str = input("Masukkan Suhu (°C)     : ")

# Pengolahan Data dan Konversi
try:
    celsius = float(celsius_str)
    
    # Rumus Konversi Suhu
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    
    # Penentuan Kondisi Ruangan
    if celsius >= 30:
        kondisi = "PANAS"
    elif celsius >= 20:
        kondisi = "NORMAL / SEJUK"
    else:
        kondisi = "DINGIN"
        
    # Output Hasil menggunakan String Concatenation (+)
    print()
    print("-" * 40)
    print("HASIL PENGUKURAN DAN KONVERSI")
    print("-" * 40)
    print("Operator System : " + nama_operator)
    print("Suhu Celcius    : " + str(celsius) + " °C")
    print("Suhu Fahrenheit : " + str(fahrenheit) + " °F")
    print("Suhu Kelvin     : " + str(kelvin) + " K")
    print("Kondisi Ruangan : " + kondisi)
    print("\\ // \\\\\\ /// " + "Selesai Diproses " + "/// \\\\\\ // \\")
    
except ValueError:
    print("\n[ERROR] Input suhu harus berupa angka!")