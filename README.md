# 🔐 SecureChat-X

SecureChat-X is a multi-user encrypted chat system designed to demonstrate secure communication principles, authentication mechanisms, and real-time networking in cybersecurity applications.

## 🚀 Overview

SecureChat-X provides a secure client-server messaging environment with:

• User authentication (registration & login)
• Password hashing
• Encrypted message transmission
• Real-time multi-user communication
• Asynchronous networking using WebSockets

This project was built as a hands-on cybersecurity exercise to explore secure system design and threat-aware communication.

---

## 🛡️ Security Features

🔐 Encrypted Messaging  
All messages are encrypted using symmetric encryption before transmission.

👤 Authentication System  
Users must register and log in before accessing the chat.

🔑 Password Hashing  
Passwords are securely hashed before storage.

🌐 Secure Communication Channel  
Uses WebSockets for real-time communication.

---

## 🧠 Architecture

Client ↔ Server model

1. Authentication Phase (plaintext for login)
2. Secure Messaging Phase (encrypted communication)

---


## ⚙️ Installation

### 1. Clone repository
git clone https://github.com/yumna-ux/SecureChat-X

cd SecureChat-X

### 2. Install dependencies
pip install -r requirements.txt

---

## ▶️ Usage

### Start server
python server.py

### Start clients (in separate terminals)
python client.py

Register users → login → start chatting securely.

---

## 🎯 Purpose

This project demonstrates:

• Secure software design  
• Cryptography basics  
• Network programming  
• Asynchronous communication  
• Cybersecurity fundamentals  

---

## 📌 Future Improvements

• Threat detection system  
• Brute-force attack monitoring  
• Admin dashboard  
• End-to-end key exchange  
• Web-based interface  

---

## 👩‍💻 Author

Yumna Mohammed  
Cybersecurity & Technology Enthusiast
