from phe import paillier
import time
import sys 

# get the start time
st = time.time()

# Generate a public and private key pair
public_key, private_key = paillier.generate_paillier_keypair()

# get the end time
et = time.time()

# get the execution time
elapsed_time1 = et - st
print('Execution time:', elapsed_time1, 'seconds')

# get the start time
start = time.time()

# Encrypt a list of numbers
encryptedNums = [public_key.encrypt(num) for num in [10, 20, 30]]

# get the end time
etaaa = time.time()

# get the execution time
elapsed_time2 = etaaa - start
print('Execution time:', elapsed_time2, 'seconds')

# get the start time
sta = time.time()

# Add the encrypted numbers
encryptedSum = sum(encryptedNums)

# get the end time
eta = time.time()

# get the execution time
elapsed_time3 = eta - sta
print('Execution time:', elapsed_time3, 'seconds')

# get the start time
star = time.time()

# Decrypt the sum
decryptedSum = private_key.decrypt(encryptedSum)

# get the end time
etaa = time.time()

# get the execution time
elapsed_time4 = etaa - star
print('Execution time:', elapsed_time4, 'seconds')

print(decryptedSum) 

# Encrypt a number
encryptedNum = public_key.raw_encrypt(10)

# get the start time
startt = time.time()

# Multiply the ciphertext with a plaintext
encryptedProd = encryptedNum * 5

# get the end time
etaaaa = time.time()

# get the execution time
elapsed_time5 = etaaaa - startt
print('Execution time:', elapsed_time5, 'seconds')

# Decrypt the product
decryptedProd = private_key.raw_decrypt(encryptedProd)

# calculate average elapsed time
average_elapsed_time = (elapsed_time1 + elapsed_time2 + elapsed_time3 + elapsed_time4 + elapsed_time5 ) / 5
print('Average execution time:', average_elapsed_time, 'seconds')

print(sys.getsizeof(10))
print(sys.getsizeof(encryptedNums[0]))
print(sys.getsizeof(private_key) + sys.getsizeof(public_key))
