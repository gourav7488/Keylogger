# 🔐 Keylogger – Mini Project (6th Semester)

This repository contains a **Keylogger** developed as part of my mini project during the 6th semester of my BTech in Computer Science and Engineering. The project focuses on building a basic keystroke logging tool using Python to demonstrate how such tools operate and their implications in cybersecurity.

> ⚠️ **Disclaimer**: This keylogger is intended for **educational and ethical research purposes only**. Using this tool on systems without proper authorization is illegal and unethical. Please use it responsibly.

---

## 📌 Project Overview

A **Keylogger** is a surveillance tool that records every keystroke made on a keyboard. This project was built to explore how keyloggers work under the hood and understand the threats they pose from a cybersecurity perspective. The application runs in the background, capturing keystrokes and storing them in a log file (with optional email functionality).

---

## 🚀 Features

- ⌨️ Captures all keyboard inputs
- 🕒 Logs each keystroke with timestamps
- 📁 Stores logs locally in a hidden or specified file
- 📤 Optional feature to send logs via email (SMTP)
- 🖥️ Runs in stealth mode (background execution)
- 🧪 Lightweight, clean, and efficient Python code

---

## 🧰 Tech Stack

- **Language**: Python 3.x
- **Libraries Used**:
  - `pynput` – For listening to keyboard events
  - `logging` – For structured log handling
  - `smtplib` – For optional email delivery
  - `os`, `threading`, `time` – Utility modules for operations

---

## 📦 Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/keylogger-mini-project.git
cd keylogger-mini-project
```


### Step 2: Install dependencies
```bash
pip install pynput
```

### Step 3: Run the Keylogger
```bash
python keylogger.py
```

## ⚙️ Configuration

You can customize the keylogger to fit your needs:

- Log file output location
- Enable email delivery (edit SMTP setting in script)
- Add script to strtup (windows/Linux) for demo purpose
- 
---

## 🔐 Ethical Use Cases

This project can be used for:

- 📚 **Educational Demonstration** – Learn how keyloggers work.
- 🧠 **Malware Analysis Practice** – Understand how attackers use similar tools.
- 🧪 **Testing Defensive Tools** – Analyze how antivirus, EDR, or firewalls detect and block keyloggers.
- 🛡️ **Endpoint Protection Study** – Understand the role of monitoring and detection systems.

---

## 🎓 Learnings

Through this mini project, I learned:

- 🎹 How to capture keystrokes using `pynput` in Python
- 🧵 How to run tasks in the background using threading
- 🕵️‍♂️ How offensive tools behave, and how they can be used to train defensive techniques
- 🔐 The importance of using such tools ethically and responsibly

---

## 👨‍💻 Author

**Your Name**  
BTech CSE | 6th Semester  
Cybersecurity Enthusiast | Ethical Hacker | Bug Bounty Hunter

### 🔗 Connect with me:
- [LinkedIn](https://www.linkedin.com/in/gourav-kumar-438670291/)
- [Medium](https://medium.com/@spidergk)
- [YouTube - RootForce](https://www.youtube.com/@spidergk108)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
