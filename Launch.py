from RSA import generateRandomPrimeNumber, generatePublicKey, generatePrivateKey, encryption, decryption

p = generateRandomPrimeNumber()
q = generateRandomPrimeNumber()
publicKey = generatePublicKey(p*q, p, q)
privateKey = generatePrivateKey(p, q, publicKey)

message = input("Enter a sentence you want to encrypt:")
cipher = encryption(publicKey, p*q, message)
decryptedValue = decryption(privateKey, p, q, cipher)

print(f"Private Key = {privateKey}")
print(f"Public Key = {publicKey}")
print(f"n = {p*q}")
print(f"encrypted value of text = {cipher}")
print(f"decrypted value of text = {decryptedValue}")