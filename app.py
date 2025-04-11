from flask import Flask, render_template, request, redirect
from encryption import encrypt_data, decrypt_data
from database import create_table, insert_user, fetch_users

app = Flask(__name__)
create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Encrypt the password before saving
        encrypted_password = encrypt_data(password)
        
        # Save to database (SQL Injection Protected)
        insert_user(username, encrypted_password)
        message = '✅ User securely added to cloud DB!'
        
    users = fetch_users()
    
    # Decrypt passwords for display (optional)
    decrypted_users = [(user[0], decrypt_data(user[1])) for user in users]
    
    return render_template('index.html', message=message, users=decrypted_users)

if __name__ == '__main__':
    app.run(debug=True)
