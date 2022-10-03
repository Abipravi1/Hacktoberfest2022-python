import jwt

key = "your_secret"
encoded = jwt.encode({"some": "payload"}, key, algorithm="HS256")
print(encoded)

decoded = jwt.decode(encoded, key, algorithms="HS256")
print(decoded)