# NAMA  : 
# KELAS : 
# ---------------------------------------------------------
# LATIHAN: REVIEW LIST PYTHON
#Diberikan sebuah data acak nilai ujian siswa. Buatlah program yang mengurutkan data tersebut 
#dari nilai tertinggi ke terendah. Kemudian, pisahkan 3 nilai tertinggi sebagai penerima beasiswa, 
#dan hapus nilai terendah (nilai di bawah 60) karena dianggap tidak lulus. 
#Gunakan data awal berikut: nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
# ---------------------------------------------------------

# OUTPUT
#Data nilai asli: [75, 55, 90, 85, 45, 95, 80] 
#Data setelah diurutkan (Descending): [95, 90, 85, 80, 75, 55, 45] 
#Tiga nilai tertinggi (Penerima Beasiswa): [95, 90, 85] 
#Daftar nilai yang lulus: [95, 90, 85, 80, 75]
# ---------------------------------------------------------

# Tulis kodemu di bawah ini:
nilai_ujian = [75, 55, 90, 85, 45, 95, 80]

print("Data nilai asli:", nilai_ujian)

nilai_urut = sorted(nilai_ujian, reverse=True)
print("Data setelah diurutkan:", nilai_urut)

beasiswa = nilai_urut[:3]
print("Tiga nilai tertinggi (Penerima Beasiswa):", beasiswa)

lulus = [nilai for nilai in nilai_urut if nilai >= 60]
print("Daftar nilai yang lulus:", lulus)