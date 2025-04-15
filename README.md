# 🛡️ Python Keylogger with Email Reporting

This is a simple yet powerful keylogger written in Python.
It captures every keystroke made on the keyboard and periodically sends the logged data to your Gmail account.
This tool is intended strictly for **educational and ethical purposes** such as parental control, penetration testing, and system monitoring (with proper authorization).

---

## 📦 Features

- ✅ Records all keyboard keystrokes
- ✅ Handles special keys like Enter, Backspace, Tab, etc.
- ✅ Sends logs to your Gmail every X seconds
- ✅ Stores logs locally as backup
- ✅ Timestamped logs for easier tracking
- ✅ Graceful error handling
- ✅ Simple and modular code structure

---

## 🚀 Usage

# 1. Clone the repository
git clone https://github.com/yourusername/python-keylogger.git
cd python-keylogger

# 2. Open main.py and add your Gmail & App Password
#    Replace:
#    EMAIL_ADDRESS = "your_email@gmail.com"
#    EMAIL_PASSWORD = "your_app_password"

# 3. Run the keylogger
python main.py

---

## ✅ What happens:

- Keystrokes are captured.
- Logs are sent to your email every 2 minutes (or the interval you set).
- If email sending fails, logs are saved locally.
