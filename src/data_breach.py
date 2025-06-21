users = {
    'user1': 'password123',
    'admin': 'admin1234'
}
def simulate_data_breach(user_db):
    print("Data breached! Berikut informasi yang bocor:")
    for username, password in user_db.items():
        print(f"Username: {username}, Password: {password}")

simulate_data_breach(users)
