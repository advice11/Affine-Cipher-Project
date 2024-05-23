# program_enkripsi.py

def gcd(a, b):
    """Fungsi untuk mengembalikan pembagi terbesar dari a dan b."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def affine_encrypt(plaintext, a, b):
    """Fungsi untuk mengenkripsi plaintext menggunakan Affine Cipher."""
    m = 26  # Panjang alfabet (untuk huruf Inggris)

    # Memastikan bahwa a dan m koprima
    if gcd(a, m) != 1:
        raise ValueError("a dan 26 tidak koprima. Pilih 'a' yang berbeda.")

    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Mengonversi karakter ke indeks alfabet (0-25)
            x = ord(char.lower()) - ord('a')
            # Menghitung karakter terenkripsi menggunakan formula Affine Cipher
            encrypted_char = (a * x + b) % m
            # Mengonversi kembali ke karakter dan menambahkan ke teks terenkripsi
            encrypted_text += chr(encrypted_char + ord('a'))
        else:
            # Menjaga karakter non-alfabet tetap sama
            encrypted_text += char

    return encrypted_text
