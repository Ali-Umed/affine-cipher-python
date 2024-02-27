def egcd(a, b):
    """
    Extended Euclidean Algorithm.
    Returns a tuple (g, x, y) such that a*x + b*y = g = gcd(a, b).
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    """
    Modular Multiplicative Inverse.
    Returns the modular multiplicative inverse of a modulo m, if it exists.
    """
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def affine_encrypt(text, key):
    """
    Encrypts the given text using the Affine Cipher.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Encrypt each alphabet character
            if char.isupper():
                result += chr(((key[0] * (ord(char) - 65) + key[1]) % 26) + 65)
            else:
                result += chr(((key[0] * (ord(char) - 97) + key[1]) % 26) + 97)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

def affine_decrypt(ciphertext, key):
    """
    Decrypts the given ciphertext using the Affine Cipher.
    """
    result = ""
    for char in ciphertext:
        if char.isalpha():
            # Decrypt each alphabet character
            if char.isupper():
                result += chr(((modinv(key[0], 26) * (ord(char) - 65 - key[1])) % 26) + 65)
            else:
                result += chr(((modinv(key[0], 26) * (ord(char) - 97 - key[1])) % 26) + 97)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    return result

# Example usage:
text = "Hello World"
print("Orginal is :", text)
key = (5, 8)  # Example key: (a, b)
encrypted_text = affine_encrypt(text, key)
print("Encrypted is :", encrypted_text)
decrypted_text = affine_decrypt(encrypted_text, key)
print("Decrypted is :", decrypted_text)


# we have 2 type off errors for gcs error are 

# Invalid Modular Multiplicative Inverse:

# If the modular multiplicative inverse of the first key a modulo 26 does not exist, decryption will fail.
# Example: Let's say we have a key (a, b) where a = 2 and b = 3. The modular multiplicative inverse of a modulo 26 is 13, but 2 does not have a modular multiplicative inverse modulo 26. Thus, decryption with this key pair will fail.
# GCD of a and 26 is not 1:

# For the encryption and decryption to work correctly, the greatest common divisor (GCD) of the first key a and 26 must be 1.
# Example: Let's consider a key (a, b) where a = 4 and b = 5. Here, the GCD of 4 and 26 is 2, which is not 1. Thus, decryption with this key pair will fail.

#  error for key.

# Invalid Key Range:
# If the keys a and b are not within the valid range, decryption might produce incorrect results.
# Example: Let's say we have a key (a, b) where a = 27 and b = 3. Here, a is out of the valid range [1, 25]. Similarly, if b is not in the range [0, 25], decryption might fail.

# Incorrect Key Pair:
# Using an incorrect key pair (a, b) for decryption, which was not used for encryption, will result in incorrect decryption.
# Example: If the ciphertext was encrypted using a key (3, 7), attempting to decrypt it with a different key pair such as (5, 10) will produce incorrect results.
