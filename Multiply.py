#To perform multiplication of one ciphertext with one plaintext, 
#we need to use the raw_encrypt() method instead of encrypt() method provided by paillier library. 

from phe import paillier
import time

# Generate a public and private key pair
public_key, private_key = paillier.generate_paillier_keypair()

# Encrypt a number
encryptedNum = public_key.raw_encrypt(10)

# get the start time
start = time.time()

# Multiply the ciphertext with a plaintext
encryptedProd = encryptedNum * 5

# get the end time
etaaa = time.time()

# get the execution time
elapsed_time2 = etaaa - start
print('Execution time:', elapsed_time2, 'seconds')

# Decrypt the product
decryptedProd = private_key.raw_decrypt(encryptedProd)

print(decryptedProd)
