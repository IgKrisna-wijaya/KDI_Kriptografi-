def rotl(x, y, w=32):
    return ((x << (y & (w-1))) & (2**w - 1)) | (x >> (w - (y & (w-1))))

def rotr(x, y, w=32):
    return (x >> (y & (w-1))) | ((x << (w - (y & (w-1)))) & (2**w - 1))

def key_expansion(key, w=32, r=12):
    b = len(key)
    u = w // 8
    c = max(1, b // u)

    # Konversi key menjadi array L
    L = [0] * c
    for i in range(b-1, -1, -1):
        L[i//u] = (L[i//u] << 8) + key[i]

    # Konstanta untuk w=32
    Pw = 0xB7E15163
    Qw = 0x9E3779B9

    # Buat array S
    t = 2 * (r + 1)
    S = [0] * t
    S[0] = Pw
    for i in range(1, t):
        S[i] = (S[i-1] + Qw) % (2**w)

    # Mixing
    A = B = i = j = 0
    for k in range(3 * max(t, c)):
        A = S[i] = rotl((S[i] + A + B) % (2**w), 3, w)
        B = L[j] = rotl((L[j] + A + B) % (2**w), (A + B), w)
        i = (i + 1) % t
        j = (j + 1) % c

    return S

def rc5_encrypt(block, S, w=32, r=12):
    A, B = block

    A = (A + S[0]) % (2**w)
    B = (B + S[1]) % (2**w)

    for i in range(1, r+1):
        A = (rotl(A ^ B, B, w) + S[2*i]) % (2**w)
        B = (rotl(B ^ A, A, w) + S[2*i+1]) % (2**w)

    return A, B

def rc5_decrypt(block, S, w=32, r=12):
    A, B = block

    for i in range(r, 0, -1):
        B = rotr((B - S[2*i+1]) % (2**w), A, w) ^ A
        A = rotr((A - S[2*i]) % (2**w), B, w) ^ B

    B = (B - S[1]) % (2**w)
    A = (A - S[0]) % (2**w)

    return A, B

# Key 16 byte (128 bit)
key = b"Mahasiswa_Teknik"

# Key schedule
S = key_expansion(key)

text = "nyobadlu"

# Ubah ke bytes
data = text.encode()

# Memastikan panjang 8 byte
if len(data) != 8:
    raise ValueError("Plaintext harus 8 karakter (8 byte)")

# Bagi menjadi dua 32-bit
A = int.from_bytes(data[:4], byteorder="little")
B = int.from_bytes(data[4:], byteorder="little")

plaintext = (A, B)

print("Plaintext (integer):", plaintext)

# Encrypt
cipher = rc5_encrypt(plaintext, S)
print("Hasil_enkripsi:", cipher)

# Decrypt
decrypted = rc5_decrypt(cipher, S)
print("Hasil_dekripsi:", decrypted)

A, B = decrypted

# Ubah kembali ke bytes (4 byte + 4 byte)
result_bytes = A.to_bytes(4, byteorder="little") + B.to_bytes(4, byteorder="little")

# Ubah bytes ke string
result_text = result_bytes.decode()
print("Hasil decrypt (text):", result_text)
