from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

p = getPrime(256)
q = getPrime(256)

n = p * q
print()
tot = (p - 1) * (q - 1)

e = 65537
d = pow(e, -1, tot)

print("n:", n)
print("e:", e)
print("d:", d)


