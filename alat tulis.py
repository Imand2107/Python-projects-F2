# Harga seunit pensel, pen, gunting, pemadam dan pembaris
pensel = 1
pen = 2
gunting = 3
pemadam = 1.5
pembaris = 1.2

# Bilangan pensel, pen, gunting, pemadam dan pembaris dimasukkan oleh pengguna
bil_pensel = int (input ("Masukkan bilangan pensel yang diperlukan: "))
bil_pen = int (input("Memasukkan bilanggan pen yang diperlukan: "))
bil_gunting = int (input("Masukkan bilanggan gunting yang diperlukan: "))
bil_pemadam = int (input("Masukkan bilanggan pemadam yang diperlukan: "))
bil_pembaris = int (input("Masukkan bilanggan pembaris yang diperlukan: "))

# Atur cara mengira harga
jum_pensel = pensel * bil_pensel
jum_pen = pemadam * bil_pen
jum_gunting = pemadam * bil_gunting
jum_pemadam = pemadam * bil_pemadam
jum_pembaris = pembaris * bil_pembaris

# Atur cara mengira jumlah kos
jum_kos = jum_pensel + jum_pen + jum_gunting + jum_pemadam * jum_pembaris

# Atur cara paparkan kos
print ("\nJumlah kos untuk alat tulis: RM"+jum_kos)