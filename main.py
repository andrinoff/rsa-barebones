def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res

def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1

# RSA Key Generation
def generateKeys():
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            input(f"Chosen e: {e}")
            break

    print(f"Compute d such that e * d ≡ 1 (mod phi(n))")
    d = modInverse(e, phi)
    input(f"Computed d: {d}")
    return e, d, n

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(m, e, n):
    print("Encrypting: Ciphertext (C) = M^e mod n")
    return power(m, e, n)

def decrypt(c, d, n):
    print("Decrypting: Plaintext (M) = C^d mod n")
    return power(c, d, n)

if __name__ == "__main__":
    e, d, n = generateKeys()
  
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    M = int(input("Enter message M (as an integer): "))
    print(f"Original Message: {M}")

    C = encrypt(M, e, n)
    input(f"Encrypted Message: {C}")

    # Decrypt the message
    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")
