from tinydb import TinyDB, Query
import hashlib

print("Sign UP Page")
username = input("Enter Username: ")
password = input("Password: ")

hash = hashlib.sha256(str.encode(password)).hexdigest()


db = TinyDB('credentials.json')

q = Query()

result = db.search(q.name == username)

if len(result) > 0:
    print("Username already exists")
else:
    db.insert({'name': username, 'hash': hash})
    print("Sign UP successful")
