# Implementasi Algoritma RC5 (Python)

Program ini merupakan implementasi sederhana dari algoritma kriptografi **RC5 (Rivest Cipher 5)** menggunakan bahasa pemrograman **Python**. Program dibuat tanpa menggunakan library enkripsi eksternal sehingga seluruh proses kriptografi diimplementasikan secara manual sesuai dengan instruksi tugas.

Program ini mendemonstrasikan proses **Key Expansion, Enkripsi, dan Dekripsi** menggunakan parameter **RC5-32/12/128**, yang berarti ukuran word 32 bit, jumlah ronde enkripsi 12 ronde, dan panjang key 128 bit (16 byte).

## Cara Menjalankan Program

Pastikan Python sudah terinstall di komputer. Untuk mengeceknya jalankan perintah berikut di terminal atau command prompt:

python --version atau python3 --version

Jika Python belum terinstall, download melalui situs resmi berikut:

https://www.python.org/downloads/

Setelah Python terinstall, download atau clone repository yang berisi source code program ini dengan perintah berikut:

git clone https://github.com/USERNAME/NAMA_REPOSITORY.git

Masuk ke folder project dengan perintah:

cd NAMA_REPOSITORY

Kemudian jalankan program dengan perintah:

python rc5_demo.py atau python3 rc5_demo.py

## Input Program

Program menggunakan key dan plaintext yang sudah ditentukan di dalam kode jika ingin mengubah key atau plaintext ubah saja didalam code.

Key yang digunakan:
Mahasiswa_Teknik (pastikan jumlah charakter berkelipatan 4)

Plaintext yang digunakan:
nyobadlu (pastikan 8 charakter)

## Output Program

Program akan menampilkan tahapan proses RC5 secara bertahap, seperti proses key expansion, proses enkripsi pada setiap ronde, dan proses dekripsi.

Contoh tampilan output program:

===== KEY EXPANSION =====  
Key: b'Mahasiswa_Teknik'  
Subkey pertama: [...]  

Plaintext (integer): (1651470702, 1970037857)

===== ENKRIPSI =====

Round 1  
A = ...  
B = ...

Round 2  
A = ...  
B = ...

...

===== DEKRIPSI =====

Round decrypt 12  
A = ...  
B = ...

Hasil decrypt (text): nyobadlu

Output tersebut menunjukkan bagaimana plaintext diubah menjadi ciphertext melalui beberapa ronde enkripsi dan kemudian didekripsi kembali menjadi plaintext semula.

## Struktur Program

Program terdiri dari beberapa fungsi utama yaitu rotl() yang melakukan rotasi bit ke kiri, rotr() yang melakukan rotasi bit ke kanan, key_expansion() yang menghasilkan subkey yang digunakan pada setiap ronde enkripsi, rc5_encrypt() yang melakukan proses enkripsi plaintext menjadi ciphertext, dan rc5_decrypt() yang melakukan proses dekripsi ciphertext kembali menjadi plaintext.

## Tujuan Program

Program ini dibuat untuk mendemonstrasikan cara kerja algoritma kriptografi **RC5** secara langkah demi langkah sebagai bagian dari tugas mata kuliah **Kriptografi**.

## Demonstrasi

Demo.mkv


## Author

Nama : Ig.Krisna Wijaya Prihandono
NIM : 24051204032 
Algoritma : RC5
