def cari_mahasiswa(data, nim):
    if nim in data:
        print("Data", data[nim]["nama"], "ditampilkan")
        print("NIM   :", nim)
        print("Nama  :", data[nim]["nama"])
        print("Kelas :", data[nim]["kelas"])
        print("Nilai :", data[nim]["nilai"])
    else:
        print("Data tidak ditemukan")


def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0
    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# TEST CASE 1: Pencarian tersedia
print("TEST CASE 1: Pencarian A003")
cari_mahasiswa(data_mahasiswa, "A003")
print()


# TEST CASE 2: Pencarian tidak tersedia
print("TEST CASE 2: Pencarian A999")
cari_mahasiswa(data_mahasiswa, "A999")
print()


# TEST CASE 3: Pembaruan nilai A002 menjadi 82
print("TEST CASE 3: Pembaruan Nilai")
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai A002 berubah menjadi:",
      data_mahasiswa["A002"]["nilai"])
print()


# TEST CASE 4: Penambahan data A006
print("TEST CASE 4: Penambahan Data")
data_mahasiswa["A006"] = {
    "nama": "Fani",
    "kelas": "B",
    "nilai": 90
}

if "A006" in data_mahasiswa:
    print("Key A006 tersedia setelah ditambahkan")
print()


# TEST CASE 5: Rekap menggunakan items()
print("TEST CASE 5: Rekap Data Mahasiswa")
for nim, data in data_mahasiswa.items():
    print(nim, data)
print()


# TEST CASE TAMBAHAN: Rata-rata nilai
print("Rata-rata nilai mahasiswa:",
      rata_rata_nilai(data_mahasiswa))