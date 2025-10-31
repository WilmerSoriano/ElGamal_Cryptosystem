"""
    Public over the channel:
        p =  A large prime number
        r = A primative root mod (p)
"""

#1. Key-generation:
    #1. Select a private-key X < p-1

    #2. Compute for Y = r^X mod(p)

#2. Encryption:
    #1. Some message(M) must be M < p

    #2. At random select k < p-1

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

