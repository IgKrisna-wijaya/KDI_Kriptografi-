def rotl(x, y, w=32):
    return ((x << (y & (w-1))) & (2**w - 1)) | (x >> (w - (y & (w-1))))

def rotr(x, y, w=32):
    return (x >> (y & (w-1))) | ((x << (w - (y & (w-1)))) & (2**w - 1))


def key_expansion(key, w=32, r=12):

    print("\n===== KEY EXPANSION =====")
    b = len(key)
    u = w // 8
    c = max(1, b // u)
    print("Key:", key)
    print("Panjang key:", b, "byte")
    # Konversi key menjadi array L
    L = [0] * c
    for i in range(b-1, -1, -1):
        L[i//u] = (L[i//u] << 8) + key[i]
    print("Array L:", L)
    # Konstanta RC5
    Pw = 0xB7E15163
    Qw = 0x9E3779B9

    t = 2 * (r + 1)
    S = [0] * t
    S[0] = Pw

    for i in range(1, t):
        S[i] = (S[i-1] + Qw) % (2**w)

    print("Subkey pertama:", S[:5])

    # Mixing tetap dilakukan tapi tidak ditampilkan
    A = B = i = j = 0
    for k in range(3 * max(t, c)):
        A = S[i] = rotl((S[i] + A + B) % (2**w), 3, w)
        B = L[j] = rotl((L[j] + A + B) % (2**w), (A + B), w)
        i = (i + 1) % t
        j = (j + 1) % c

    return S


def rc5_encrypt(block, S, w=32, r=12):

    print("\n===== ENKRIPSI =====")
    A, B = block
    print("A awal:", A)
    print("B awal:", B)
    A = (A + S[0]) % (2**w)
    B = (B + S[1]) % (2**w)
    print("\nSetelah initial key addition")
    print("A =", A)
    print("B =", B)

    for i in range(1, r+1):
        A = (rotl(A ^ B, B, w) + S[2*i]) % (2**w)
        B = (rotl(B ^ A, A, w) + S[2*i+1]) % (2**w)
        print("\nRound", i)
        print("A =", A)
        print("B =", B)

    return A, B


def rc5_decrypt(block, S, w=32, r=12):
    print("\n===== DEKRIPSI =====")
    A, B = block
    print("Ciphertext:", A, B)
    for i in range(r, 0, -1):
        B = rotr((B - S[2*i+1]) % (2**w), A, w) ^ A
        A = rotr((A - S[2*i]) % (2**w), B, w) ^ B
        print("\nRound decrypt", i)
        print("A =", A)
        print("B =", B)

    B = (B - S[1]) % (2**w)
    A = (A - S[0]) % (2**w)
    print("\nSetelah final subtraction")
    print("A =", A)
    print("B =", B)

    return A, B

key = b"Mahasiswa_Teknik"

S = key_expansion(key)

text = "nyobadlu"

data = text.encode()

if len(data) != 8:
    raise ValueError("Plaintext harus 8 karakter")

A = int.from_bytes(data[:4], byteorder="little")
B = int.from_bytes(data[4:], byteorder="little")
plaintext = (A, B)
print("\nPlaintext (integer):", plaintext)
cipher = rc5_encrypt(plaintext, S)
print("\nHasil_enkripsi:", cipher)
decrypted = rc5_decrypt(cipher, S)
print("\nHasil_dekripsi:", decrypted)
A, B = decrypted
result_bytes = A.to_bytes(4, byteorder="little") + B.to_bytes(4, byteorder="little")
result_text = result_bytes.decode()
print("\nHasil decrypt (text):", result_text)
