import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users_secure = {
    'user1': hash_password('password123'),
    'admin': hash_password('admin1234')
}

def login(username, password):
    if username in users_secure:
        if users_secure[username] == hash_password(password):
            print("Login berhasil!")
        else:
            print("Password salah!")
    else:
        print("Username tidak ditemukan!")

login('user1', 'password123')
login('user1', 'salahpassword')

def simulate_secure_breach(user_db):
    print("\n Data breached (versi aman)! Hash yang bocor:")
    for username, password_hash in user_db.items():
        print(f"Username: {username}, Password Hash: {password_hash}")

simulate_secure_breach(users_secure)
