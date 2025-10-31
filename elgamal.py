"""
    Overview:
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
"""

"""
    Public over the channel:
        p =  A large prime number
        r = A primative root mod (p)
"""

#1. Key-generation:
    #1. Select a private-key(X) as the following: X < p-1

    #2. Compute for Y = r^X mod(p)

#2. Encryption:
    #1. Some message(M) must be M < p

    #2. At random select private-key(k) as the following: k < p-1

    #3. Compute the following:
        # K = Y^k mod(p)

        # C1 = r^k mod(p)
         
        # C2 = K*M mod(p)

    #4. Return (C1, C2)

#3. Decryption:
    #1. Receive (C1,C2)

    #2. Compute the following: K = C1^X mod(p)

    #3. Compute the following: M = C2*K^-1 mod(p)

    #4. Return the message


if __name__ == '__main_':

