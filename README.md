Server Monitoring and Alerting System
This project consists of a shell script and a Python script designed to monitor server resource usage (CPU, memory, and disk) and send email alerts if any usage exceeds a specified threshold level.

Usage
Shell Script (monitor_server.sh)
Description: This shell script gathers server usage details and compares them with a specified threshold level. If any of the resource usages exceed the threshold, it triggers an email alert using the Python script.

Instructions:

Ensure the shell script and Python script are executable (chmod +x server_monitor.sh send_email.py).
Run the shell script with ./monitor_server.sh to monitor server resources.
You can set the threshold level directly in the script itself.
Python Script (send_email.py)
Description: This Python script sends email alerts if any server resource usage exceeds a specified threshold level.

Instructions:

Ensure the Python script is executable (chmod +x send_email.py).
The script should be used internally by the shell script and doesn't require manual execution.
Dependencies
Shell Script: No external dependencies required.
Python Script: Requires Python 3 and the smtplib library for sending emails.
Configuration
Email Configuration: Modify the sender_email, receiver_email, and password variables in send_email.py to match your email configuration.
Threshold Level: Adjust the threshold variable in monitor_server.sh to set the desired threshold level for resource usage.
