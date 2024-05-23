# program_kriptoanalisis.py

def gcd(a, b):
    """Fungsi untuk mengembalikan pembagi terbesar dari a dan b."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mod_inverse(a, m):
    """Fungsi untuk menemukan invers modular dari a dengan modulo m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Tidak ada invers modular untuk a = {a} dan m = {m}")

def affine_decrypt(ciphertext, a, b):
    """Fungsi untuk mendekripsi ciphertext menggunakan Affine Cipher."""
    m = 26  # Panjang alfabet (untuk huruf Inggris)

    # Memastikan bahwa a dan m koprima
    if gcd(a, m) != 1:
        raise ValueError("a dan 26 tidak koprima. Pilih 'a' yang berbeda.")

    # Menghitung invers modular dari a
    a_inv = mod_inverse(a, m)

    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Mengonversi karakter ke indeks alfabet (0-25)
            y = ord(char.lower()) - ord('a')
            # Menghitung karakter didekripsi menggunakan formula Affine Cipher
            decrypted_char = (a_inv * (y - b)) % m
            # Mengonversi kembali ke karakter dan menambahkan ke teks didekripsi
            decrypted_text += chr(decrypted_char + ord('a'))
        else:
            # Menjaga karakter non-alfabet tetap sama
            decrypted_text += char

    return decrypted_text

def affine_cryptanalysis(ciphertext):
    """Fungsi untuk melakukan kriptoanalisis pada ciphertext menggunakan Affine Cipher."""
    m = 26  # Panjang alfabet (untuk huruf Inggris)
    possible_solutions = []

    # Mencoba semua kemungkinan nilai a dan b
    for a in range(1, m):
        if gcd(a, m) == 1:
            a_inv = mod_inverse(a, m)
            for b in range(m):
                # Mendekripsi dengan pasangan a dan b
                decrypted_text = affine_decrypt(ciphertext, a, b)
                # Menyimpan pasangan dan hasil dekripsi
                possible_solutions.append((a, b, decrypted_text))

    return possible_solutions
