import smtplib
from email.mime.text import MIMEText
import sys

def send_email(threshold, cpu_usage, memory_usage, disk_usage):
    sender_email = "kannan742003@gmail.com"
    receiver_email = "kannakutty089@gmail.com"
    password = "wbjs yzzp llvp azjg"

    message_body = "Server Alert:\n"
    if cpu_usage > threshold:
        message_body += f"CPU Usage: {cpu_usage}%\n"
    if memory_usage > threshold:
        message_body += f"Memory Usage: {memory_usage}%\n"
    if disk_usage > threshold:
        message_body += f"Disk Usage: {disk_usage}%\n"

    message = MIMEText(message_body)
    message["Subject"] = "Server Alert"
    message["From"] = sender_email
    message["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

# Usage: python3 send_email.py threshold cpu_usage memory_usage disk_usage
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 send_email.py threshold cpu_usage memory_usage disk_usage")
        sys.exit(1)
    
    threshold = float(sys.argv[1])
    cpu_usage = float(sys.argv[2])
    memory_usage = float(sys.argv[3])
    disk_usage = float(sys.argv[4])

    send_email(threshold, cpu_usage, memory_usage, disk_usage)

