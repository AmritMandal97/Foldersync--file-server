from flask import Flask, request, send_from_directory, render_template_string, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # CHANGE THIS TO ANY RANDOM STRING

# ---- Login Credentials ----
USERNAME = "admin"
PASSWORD_HASH = generate_password_hash("Pokman2015%")

# ---- Folder to Host ----
FOLDER = r"C:\Users\ASUS\Downloads\Telegram Desktop"   # CHANGE THIS


# ------ LOGIN PAGE HTML ------
login_page = """
<!DOCTYPE html>
<html>
<body>
<h2>Login</h2>
<form method="post">
  Username:<br><input type="text" name="username"><br>
  Password:<br><input type="password" name="password"><br><br>
  <input type="submit" value="Login">
</form>
</body>
</html>
"""


# ------ HOME PAGE ------
@app.route('/')
def index():
    # If NO session => go to login
    if "logged_in" not in session:
        return redirect("/login")

    # ----- AUTO LOGOUT ON REFRESH -----
    # If user has already viewed the page once, logout
    if session.get("visited"):
        session.pop("logged_in", None)
        session.pop("visited", None)
        return redirect("/login")

    # First time visit → allow it and mark visited
    session["visited"] = True

    files = os.listdir(FOLDER)
    file_links = "<br>".join([f"<a href='/{file}'>{file}</a>" for file in files])

    return f"""
    <h2>File Server</h2>
    <a href='/logout'>Logout</a><br><br>
    {file_links}
    <br><br>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload File">
    </form>
    """


# ------ LOGIN ROUTE ------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['username']
        pwd = request.form['password']

        if user == USERNAME and check_password_hash(PASSWORD_HASH, pwd):
            session["logged_in"] = True
            return redirect("/")
        else:
            return login_page + "<p style='color:red;'>Wrong credentials!</p>"

    return login_page


# ------ LOGOUT ------
@app.route('/logout')
def logout():
    session.pop("logged_in", None)
    return redirect("/login")


# ------ FILE DOWNLOAD ------
@app.route('/<path:filename>')
def download(filename):
    if "logged_in" not in session:
        return redirect("/login")
    return send_from_directory(FOLDER, filename, as_attachment=True)


# ------ FILE UPLOAD ------
@app.route('/upload', methods=['POST'])
def upload():
    if "logged_in" not in session:
        return redirect("/login")
    f = request.files['file']
    f.save(os.path.join(FOLDER, f.filename))
    return "Uploaded! <br><a href='/'>Go Back</a>"


# ------ AUTO LOGOUT TIMER ------
@app.before_request
def session_timeout():
    session.permanent = True
    app.permanent_session_lifetime = 300   # <-- AUTO LOGOUT AFTER 300 SECONDS


app.run(port=8000)

