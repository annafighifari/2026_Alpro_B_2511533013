umur_3013 = int(input("Input umur anda: "))
sim_3013 = input("Apakah anda sudah punya sim C (y/n): ")[0]

if umur_3013 >= 17 and sim_3013 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

elif umur_3013 >= 17 and sim_3013 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

elif umur_3013 < 17 and sim_3013 == 'y':
    print("Anda belum cukup umur punya SIM")

else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program selesai")