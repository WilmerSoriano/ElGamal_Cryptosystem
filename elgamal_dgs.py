"""
ELGAMAL DIGITAL SIGNATURE SCHEME (DGS) IMPLEMENTATION
    Overview:
        * q =  A large prime number , and r = A primative root mod (q)
          both are public for anyone to see.
        
        * If X = person1 private key AND Y = public key = r^X mod(q)

        * To create a digital signature:
            - Choose a random k such that gcd(k, q-1) = 1
            - Compute s1 = r^k mod(q)
            - Compute the modular inverse of k mod(q-1)
            - Compute s2 = k^-1 * (m - X*s1) mod(q-1)
            - Send (s1, s2) along with the message

        * To verify the digital signature:
            - Receiver checks that: (Y^s1 * s1^s2) mod(q) = r^m mod(q)
            - If true, the message is authentic and untampered.

        * How does ElGamal remain secure even when q and r are public?
            - Because it is infeasible to compute the private key X or the random k
              from public values (q, r, Y, s1, s2).
            - This difficulty arises from the discrete logarithm problem,
              which becomes computationally infeasible for large primes.

        NOTE: For demonstration purposes, values are hardcoded
"""

# Used previously with elgamal.py code
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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#1. Key-generation:
def gen_keys(p, r):
    #1. Select a private-key(X) as the following: X < p-1
    private_key = 84
    if p-1 <= private_key:
        raise Exception("Value for private-key does not meet X < p-1")
    
    #2. Compute for Y = r^X mod(p)
    public_key = pow_mod(r, private_key, p)
    
    return public_key, private_key

#2. NEW === Adding digital signature ===
def sign_message(private_key, message, q, r):
    #1. choose k such that 1< k < q-1, gcd(k, q-1) = 1
    k = 77
    if gcd(k, q - 1) != 1:
        raise Exception("k is not coprime with q-1")

    #2. Compute s1 = r^k mod q
    s1 = pow_mod(r, k, q)

    #3. Compute  k^-1 mod(q-1)
    _, k_inv, _ = ext_euclidean(k, q - 1)
    k_inv = k_inv % (q - 1)

    #4. Compute s2 = k_inv * (m - X*s1) mod(q-1)
    s2 = (k_inv * (message - private_key * s1)) % (q - 1)
    return (s1, s2)

#3. Verify digital signature
def verify_signature(public_key, message, signature, q, r):
    s1, s2 = signature

    # Compute v1 = r^m mod q
    v1 = pow_mod(r, message, q)
    # Compute v2 = Y^s1 * s1^s2 mod q
    v2 = (pow_mod(public_key, s1, q) * pow_mod(s1, s2, q)) % q

    return v1 == v2

if __name__ == "__main__":
    q = 563
    r = 5

    # 1st. Key generation
    public_key, private_key = gen_keys(q, r)

    # 2nd. Digital signature demo
    message = 123
    print("Creating digital signature for message m =", message)
    signature = sign_message(private_key, message, q, r)
    print("Signature (S1, S2):", signature)

    print("=" * 45)
    # [CASE 1] The signature is valid
    print("[CASE 1] Verifying signature...")
    valid = verify_signature(public_key, message, signature, q, r)
    print("Verification result:", valid)

    # [CASE 2] Adversary attempts to tamper with the message
    print("=" * 45)
    tamp_message = 124
    print("[CASE 2] Testing tampered message...")
    tampered = verify_signature(public_key, tamp_message, signature, q, r)
    print("Verification result :", tampered)