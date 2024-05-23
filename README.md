# Enkripsi Affine Cipher

Repository ini berisi implementasi sederhana dari algoritma enkripsi Affine Cipher dalam Python.

penggunaan fitur yang digunakan di dalam program :
1. main.py
- Menu Looping: Pengguna diberi pilihan untuk melakukan enkripsi, dekripsi, kriptoanalisis, atau keluar dari program.
- User Input: Pengguna diminta untuk memasukkan pilihan, teks, dan kunci.
- Exception Handling: Menangani kesalahan jika kunci yang dimasukkan tidak valid.
- Break Statement: Menghentikan loop jika pengguna memilih untuk keluar dari program.

2. program_enkripsi.py (Encryption Program)
- Affine Cipher Encryption: Mengenkripsi teks menggunakan Affine Cipher.
- Key Validation: Memastikan kunci yang dimasukkan oleh pengguna valid.

3. program_dekripsi.py (Decryption Program)
- Affine Cipher Decryption: Mendekripsi teks menggunakan Affine Cipher.
- Key Validation: Memastikan kunci yang dimasukkan oleh pengguna valid.
- Inverse Modular Calculation: Menghitung invers modular untuk dekripsi.

4. program_kriptoanalisis.py (Cryptanalysis Program)
- Affine Cipher Cryptanalysis: Melakukan kriptoanalisis untuk mencari kemungkinan solusi.
- Brute Force Attack: Mencoba semua kemungkinan nilai kunci 𝑎 dan 𝑏 untuk mencari solusi.

## Cara Menggunakan

1. Clone repository ini.
2. Jalankan `main.py` untuk memulai program.

## Persyaratan
- Python 3.x

## Instruksi Penggunaan

Setelah menjalankan `main.py`, program akan meminta Anda untuk memilih operasi yang ingin dilakukan:

1. Ketik `1` untuk Enkripsi
2. Ketik `2` untuk Dekripsi
3. Ketik `3` untuk Kriptoanalisis

atau

4. ketik `4` untuk keluar dari program

Ikuti petunjuk yang diberikan oleh program untuk memasukkan teks dan kunci yang diperlukan.

- Enkripsi :
```Program enkripsi
Pilih operasi yang ingin dilakukan:
1. Enkripsi
2. Dekripsi
3. Kriptoanalisis
4. keluar
Masukkan pilihan (1/2/3): 1
Masukkan plaintext: hello
Masukkan kunci a: 5
Masukkan kunci b: 8
Teks terenkripsi: axeeh
```

- Dekripsi :
```Program Dekripsi
Pilih operasi yang ingin dilakukan:
1. Enkripsi
2. Dekripsi
3. Kriptoanalisis
4. keluar
Masukkan pilihan (1/2/3): 2
Masukkan ciphertext: axeeh
Masukkan kunci a: 5
Masukkan kunci b: 8
Teks didekripsi: hello
```

- Kriptoanalisis :
```Program Kriptoanalisis
Pilih operasi yang ingin dilakukan:
1. Enkripsi
2. Dekripsi
3. Kriptoanalisis
4. keluar
Masukkan pilihan (1/2/3): 3
Masukkan ciphertext: axeeh
Melakukan kriptoanalisis...
a = 1, b = 0 -> axeeh
a = 1, b = 1 -> byffi
...
```

### Menjalankan Program

Terminal Text Editor :
jalankan program dibawah di direktori yang benar, dan buka terminal di text editor yang kalian pakai

```bash
python main.py
```

Terminal atau CMD Prompt : 
Navigasi ke folder proyek. Misalnya, jika Anda menyimpan folder di desktop, Anda dapat menggunakan perintah berikut di terminal:

```bash
cd path/to/your/UTS_Kriptografi
```

### Video Demo

Tonton Video Demo di link ini.

### Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT.