"""
    Overview:
        * p =  A large prime number , and r = A primative root mod (p)
        both are public for anyone to see.
        
        * If X = person1 private key AND Y = public key = r^X mod(p)

        * Then person2 uses the public-key to create a unique master key: K = Y^k mod(p)

        * Now hide the message using K master key: C2 = M*K mod(p)

        * To decrypt message: both users, at certain point, had to compute the following:
            - K = r^(k*X) mod p, which noticable when remembering:
            - K = Y^x mod(p) and K = C1^X mod(p), where both Y AND C1 compute as: = r^(k*X)
          Hence 2 private key creating 1 master key, only computed by person1 and person2

        * How does ElGamal make message secure given that public key (p and r) is made public over a channel?
            - While yes, p and r are made public for any user to view.
            - It is infeasible to compute for both private key (X or k)
              by only using public key (Y), p, and r.
            - This is possible because p is a large prime number and with also both private key being random and large
            the possibilities starts to become very large and time consuming to attack by brute force.

        NOTE for demonstration purpose the values will be hardcoded
"""

# Used previous from RSA
def ext_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = ext_euclidean(b, a % b)

        x = y1
        y = x1 - (a // b) * y1

        return gcd, x, y

def pow_mod(r, exp, p):
    result = 1
    r = r % p
    while exp > 0:
        if exp % 2 == 1:
            result = (result * r) % p
        exp = exp // 2
        r = (r * r) % p
    return result

#1. Key-generation:
def gen_keys(p, r):
    #1. Select a private-key(X) as the following: X < p-1
    private_key = 84
    if p-1 <= private_key:
        raise Exception("Value for private-key does not meet X < p-1")
    
    #2. Compute for Y = r^X mod(p)
    public_key = pow_mod(r, private_key, p)
    
    return public_key, private_key

#2. Encryption:
def encrypt(public_key, M, p, r):
    #1. Some message(M) must be M < p
    if p <= M:
        raise Exception("Length of message is longer then p")

    #2. At random select private-key(k) as the following: k < p-1
    k = 50
    if p-1 <= k:
        raise Exception("Length of message is longer then p")
    #3. Compute the following:
        # K = Y^k mod(p)
    K = pow_mod(public_key, k, p)  
        # C1 = r^k mod(p)
    C1 = pow_mod(r, k, p)
        # C2 = K*M mod(p)
    C2 = (K*M) % p
    #4. Return (C1, C2)
    return (C1, C2)

#3. Decryption:
def decrypt(private_key, r, p, cipher):
    #1. Receive (C1,C2)
    C1, C2 = ciphertext

    #2. Compute the following: K = C1^X mod(p)
    K = pow_mod(C1, private_key, p)

    #3. Compute the following: M = C2*K^-1 mod(p)
    _, K_inv, _ = ext_euclidean(K, p)

    M = (C2*K_inv) % p
    #4. Return the message
    return M

if __name__ == "__main__":
    p = 563
    r = 5

    public_key, private_key = gen_keys(p, r)
    print("Generating public-key and private-key...")

    print("="*30)
    print("Encrypting secret message!")

    M = 100
    print("Before encryption:", M)
    ciphertext = encrypt(public_key, M, p, r)
    print("After encryption:", ciphertext)

    print("="*30)
    print("Decrypting secret message!")

    M = decrypt(private_key, r, p, ciphertext)
    print("Returning Message:", M)
