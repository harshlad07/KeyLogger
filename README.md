## 🛡️ KeyWatch - Python-Based Keylogger with Email Reporting and GUI

**KeyWatch** is a simple yet powerful keylogger tool written in Python for educational and ethical testing purposes. It logs keystrokes, stores logs locally, and periodically sends reports to your email. The application also comes with a user-friendly **GUI** for easy control and configuration.

> ⚠️ This tool is strictly for **educational purposes** and authorized environments only. Do not use it unethically or without proper consent.

---

## 🧠 Features

- ✅ Logs all keyboard input (including special keys like Enter, Shift, etc.)
- 📧 Sends logs via Gmail SMTP at regular intervals
- 💾 Saves logs locally in a `Captured_Logs` folder
- 🧵 Runs in a background thread without blocking the UI
- 🖥️ User-friendly GUI built using `tkinter`
- 🛑 Graceful exit when the user closes the application window

---

## ⚙️ Requirements

- Python 3.8+
- Required Python libraries:
  - `pynput`
  - `tkinter` (standard with Python)
  
Install requirements with:

```
pip install -r requirements.txt
```

---

## 🚀 How to Use
1. Clone the Repository
```
git clone https://github.com/harshlad07/KeyLogger.git
cd KeyLogger
```
2. Run the GUI Application
```
python main.py
```
3. Input Required Details
Email: Your Gmail address
App Password: Generate an App Password here
Interval: How often (in seconds) to send the log to your email

---

## 📦 Output
Logs are stored in the Captured_Logs/ directory.
Emails will contain a timestamped snapshot of keystrokes captured since the last interval.

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork, modify, and submit a pull request. Please ensure your changes are ethical and improve the educational value of the project.

---

## ⚠️**DISCLAIMER** 🛑
THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY. DO NOT USE IT WITHOUT PROPER AUTHORIZATION.

---
