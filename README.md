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
