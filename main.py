# main.py

import program_enkripsi
import program_dekripsi
import program_kriptoanalisis

def main():
    while True:
        print("Pilih operasi yang ingin dilakukan:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Kriptoanalisis")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            plaintext = input("Masukkan plaintext: ")
            a = int(input("Masukkan kunci a: "))
            b = int(input("Masukkan kunci b: "))
            try:
                encrypted_text = program_enkripsi.affine_encrypt(plaintext, a, b)
                print(f"Teks terenkripsi: {encrypted_text}")
            except ValueError as e:
                print(e)  # Menangkap pesan kesalahan jika kunci tidak valid

        elif pilihan == '2':
            ciphertext = input("Masukkan ciphertext: ")
            a = int(input("Masukkan kunci a: "))
            b = int(input("Masukkan kunci b: "))
            try:
                decrypted_text = program_dekripsi.affine_decrypt(ciphertext, a, b)
                print(f"Teks didekripsi: {decrypted_text}")
            except ValueError as e:
                print(e)  # Menangkap pesan kesalahan jika kunci tidak valid

        elif pilihan == '3':
            ciphertext = input("Masukkan ciphertext: ")
            print("Melakukan kriptoanalisis...")
            solutions = program_kriptoanalisis.affine_cryptanalysis(ciphertext)
            for a, b, solution in solutions:
                print(f"a = {a}, b = {b} -> {solution}")

        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break  # Keluar dari loop jika pengguna memilih opsi keluar

        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")

if __name__ == "__main__":
    main()
