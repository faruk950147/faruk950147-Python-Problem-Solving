# encoding decoding

# encoding is the process of converting a string into a sequence of bytes
# decoding is the process of converting a sequence of bytes into a string

a = "Hello, World!"
encoded = a.encode()
print(encoded)

decoded = encoded.decode()
print(decoded)

# encoded = a.encode("utf-8")
# print(encoded)

# decoded = encoded.decode("utf-8")
# print(decoded)