import hashlib

# Your code here.
text = "Hello, world!"

res  = hashlib.md5(text.encode())
print(res.hexdigest())

res  = hashlib.sha1(text.encode())
print(res.hexdigest())

res  = hashlib.sha256(text.encode())
print(res.hexdigest())
