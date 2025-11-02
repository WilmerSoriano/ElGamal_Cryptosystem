# ElGamal_Cryptosystem

## Overview
This project is a **simplified implementation of the ElGamal cryptosystem** in Python.  
The main purpose of this code is **educational/reference**, helping learners understand how **ElGamal encryption** works, 
how **public and private keys** are generated, and how **modular arithmetic** and the **Extended Euclidean Algorithm** are used 
during encryption and decryption.

---

## Key Features
- Key generation using **small, hardcoded primes** (`p` and `q`) for simplicity.  
- Implementation of the **Extended Euclidean Algorithm** to calculate the modular inverse.  
- Encryption and decryption functions for integer messages.  
- Demonstrates the creation of **public and private keys**.  

---

## Limitations and Potential Improvements
This code is intentionally **simple** to focus on learning concepts. There is **significant room for improvement**, including:  
- **Random primes** (`p` and `q`) instead of hardcoded values.  
- Handling messages of **any type**, not limited by `m = p*q`.  
- Making the `k` value dynamic and prime as `p` and `q` changes .  
- Overall making the code more **dynamic and realistic** to reflect real-world ElGamal.

> The primary goal here is educational/refrence: to understand **how ElGamal generates keys**, how **public and private keys relate**, and how the **Extended Euclidean Algorithm** computes the modular inverse. Can be built upon for more robust implementations / future projects.

---
