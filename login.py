from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret123'  


users = {
    "admin": "admin123",
    "test": "test123",
    "user1": "password"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if username not in users:
            return "❌ user not found", 200
        elif users[username] != password:
            return "❌ wrong password", 200
        else:
            session['user'] = username
            return redirect(url_for('success'))

    return render_template_string('''
        <html>
        <head>
            <title>Login Project</title>
            <style>
                body {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                    color: #000;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }
                .login-container {
                    background-color: #ffffff;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    width: 300px;
                    text-align: center;
                }
                h2 {
                    margin-bottom: 20px;
                    color: #333;
                }
                label {
                    display: block;
                    margin-bottom: 5px;
                    text-align: left;
                }
                input[type="text"], input[type="password"] {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 15px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input[type="submit"] {
                    background-color: #000;
                    color: #fff;
                    border: none;
                    padding: 10px;
                    width: 100%;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #333;
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <h2>🔐 login Project</h2>
                <form method="post">
                    <label>username:</label>
                    <input type="text" name="username" required>
                    
                    <label>passwoord:</label>
                    <input type="password" name="password" required>
                    
                    <input type="submit" value="submit">
                </form>
            </div>
        </body>
        </html>
    ''')

@app.route('/success')
def success():
    username = session.get('user')
    if not username:
        return redirect(url_for('login'))

    return render_template_string(f'''
        <html>
        <head>
            <title>welcome</title>
            <style>
                body {{
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                    color: #000;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }}
                .success-container {{
                    background-color: #ffffff;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    text-align: center;
                }}
                h2 {{
                    color: #333;
                }}
                p {{
                    font-size: 18px;
                }}
            </style>
        </head>
        <body>
            <div class="success-container">
                <h2>✅ signed in successfully</h2>
                <p>welcome<strong>{username}</strong> 👋</p>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
