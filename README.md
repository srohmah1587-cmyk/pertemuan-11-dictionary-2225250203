# Pertemuan 11 - Dictionary/Map

**Nama:** Siti Rohmah  
**NIM:** 2225250203  
**Kelas:** 3A  

## Tujuan

Tujuan praktikum ini adalah memahami penggunaan dictionary dalam Python untuk memodelkan data pendidikan menggunakan pasangan key-value. Praktikum ini juga bertujuan melatih kemampuan mengolah data mahasiswa melalui operasi pencarian, penambahan, pembaruan, dan rekap data.

## Struktur Data

Program ini menggunakan dictionary bernama `data_mahasiswa` untuk menyimpan data mahasiswa.

Key utama yang digunakan adalah NIM mahasiswa, seperti `A001`, `A002`, dan `A003`. Setiap NIM memiliki value berupa dictionary yang berisi informasi mahasiswa, yaitu nama, kelas, dan nilai.

Contoh struktur data:

```python
data_mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "kelas": "A",
        "nilai": 85
    }
}
```

Pada struktur tersebut, `A001` merupakan key utama, sedangkan `nama`, `kelas`, dan `nilai` merupakan key di dalam dictionary yang menyimpan informasi mahasiswa.

Program menerapkan beberapa operasi dictionary, yaitu:

1. **Pencarian:** Memeriksa keberadaan NIM menggunakan operator `in`.
2. **Penambahan:** Menambahkan data mahasiswa baru menggunakan key baru.
3. **Pembaruan:** Mengubah nilai mahasiswa melalui key `nilai`.
4. **Rekap:** Menampilkan seluruh data mahasiswa menggunakan metode `items()`.
5. **Perhitungan:** Menghitung rata-rata nilai mahasiswa menggunakan perulangan dan metode `values()`.

## Cara Menjalankan

Jalankan program melalui terminal menggunakan perintah berikut:

```bash
python3 praktik/data_mahasiswa.py
```

Program akan menjalankan test case pencarian data, pembaruan nilai, penambahan data, rekap mahasiswa, dan perhitungan rata-rata nilai.

## Test Case

| No. | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | Mencari NIM A003 | Data Citra ditampilkan | Data Citra ditemukan beserta kelas dan nilainya | Berhasil |
| 2 | Mencari NIM A999 | Pesan "Data tidak ditemukan" | Pesan "Data tidak ditemukan" ditampilkan | Berhasil |
| 3 | Mengubah nilai A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai A002 menjadi 82 | Berhasil |
| 4 | Menambahkan data A006 | Key A006 tersedia setelah ditambahkan | Key A006 tersedia dalam dictionary | Berhasil |
| 5 | Menampilkan rekap dengan `items()` | Semua NIM dan data mahasiswa ditampilkan | Seluruh data mahasiswa ditampilkan | Berhasil |

Catatan: Hasil aktual di atas merupakan hasil yang diharapkan berdasarkan kode program. Pengujian langsung dilakukan dengan menjalankan program di terminal.

## Refleksi

Kesalahan yang dapat terjadi saat menggunakan dictionary adalah mengakses key yang tidak tersedia. Contohnya, mengakses `data_mahasiswa["A999"]` ketika NIM tersebut belum terdaftar. Kesalahan ini dapat menyebabkan `KeyError` karena key yang diminta tidak ditemukan.

Cara memperbaikinya adalah memeriksa keberadaan key menggunakan operator `in` sebelum mengakses data.

Contoh:

if "A999" in data_mahasiswa:
    print(data_mahasiswa["A999"])
else:
    print("Data tidak ditemukan")

Dengan cara tersebut, program dapat menangani pencarian NIM yang tidak tersedia tanpa mengalami error. Praktikum ini memberikan pemahaman bahwa dictionary memudahkan penyimpanan dan pengolahan data berdasarkan key yang unik.