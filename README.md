# Foldersync--file-server
Got you! Here is a **GitHub-profile–style, polished, emoji-rich, modern README** for your project.
This version looks **clean, attractive, and professional** — perfect for showing off the project on GitHub.

You can paste this directly into **README.md**.

---

# 🌐 Secure Python File Server

### A lightweight, password-protected, auto-logout enabled file server built using Flask

<div align="center">

🚀 **Secure • Fast • Minimal • Easy to Deploy**
🔐 **Login • Logout • Auto Logout • Upload • Download • Live Folder Sync**

</div>

---

## ✨ Features

* 🔐 **Login system** with hashed password (no plain text!)
* 🚪 **Logout button** for manual session end
* 🔄 **Auto Logout on refresh** for extra security
* ⏱ **Session timeout** (default 10 minutes)
* 📤 **File upload** (files instantly appear in your folder)
* 📥 **File download**
* 🔁 **Live folder sync** (add/remove files locally → instantly visible on server)
* 🌍 **Optional Cloudflare Tunnel support** for secure global access
* ⚡ Simple, clean, single-file Python project

---

## 📁 Project Structure

```
secure-file-server/
│
├── secure_server.py
└── README.md
```

---

## 🛠 Requirements

Install dependencies:

```bash
pip install flask werkzeug
```

(Optional) For online access:

```bash
pip install cloudflared
```

---

## 🚀 Getting Started

### **1️⃣ Configure your folder and password**

Inside **secure_server.py**, edit:

#### Folder you want to serve:

```python
FOLDER = r"C:\Users\YourName\MyFolder"
```

#### Login password:

```python
generate_password_hash("yourpassword")
```

#### Secret key:

```python
app.secret_key = "your_random_key_here"
```

---

### **2️⃣ Run the server**

```bash
python secure_server.py
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

## 🌐 Access the Server From Anywhere (Optional)

Using **Cloudflare Tunnel** (free, safe, encrypted):

```bash
cloudflared tunnel --url http://localhost:8000
```

Cloudflare will generate a secure HTTPS link such as:

```
https://your-random-url.trycloudflare.com
```

You can open this URL from ANY device.

---

## 🔗 Main Routes

| Route         | Description                       |
| ------------- | --------------------------------- |
| `/login`      | Login page                        |
| `/`           | Home page → file browser + upload |
| `/upload`     | Upload a file                     |
| `/logout`     | Logout user                       |
| `/<filename>` | Download file                     |

---

## 🔒 Security Features

* Password hashing (safe storage)
* Session-based authentication
* Auto logout after inactivity
* Auto logout on browser refresh
* Compatible with HTTPS via Cloudflare Tunnel

⚠️ **Never expose `http://localhost:8000` directly to the internet without Cloudflare.**

---

## 💡 Potential Enhancements

These can be added easily if you want:

* 🗑 Delete files from browser
* ✏ Rename files
* 📁 Folder navigation system
* 🎨 Dark mode UI
* 🔑 Multi-user system
* 📊 Admin dashboard
* ⚙ Auto-refresh file list
* 🔔 Real-time updates via WebSockets

Tell me anytime — I can build these for you.

---

## ❤️ Show Your Support

If you like this project, give it a ⭐ on GitHub!
It helps others discover it and motivates future upgrades.

---

## 👨‍💻 Author

Built with ❤️ and Flask.
Need custom features? Just ask — I'm here to help!

---

If you want, I can also create:

✨ A **logo/banner** for your project
✨ A **LICENSE file**
✨ A **.gitignore** ready for Python
✨ A proper **release version (v1.0.0)**
✨ A **dark theme README**

Just tell me!
