# program ini menggunakan konstanta untuk menghitung luas lingkaran
from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3013 = float(input('Masukkan nilai jari-jari: '))
luas_3013 = PI * jari_3013 * jari_3013
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3013, luas_3013))