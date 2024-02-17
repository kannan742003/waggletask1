#!/bin/bash

# Function to send email using Python
send_email() {
    python3 send_email.py "$threshold" "$cpu_usage" "$memory_usage" "$disk_usage"
}

# Gather server details
cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
memory_usage=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
disk_usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

# Set threshold level
threshold=10  # 

# Compare with threshold level
if (( $(echo "$cpu_usage > $threshold" | bc -l) )) || (( $(echo "$memory_usage > $threshold" | bc -l) )) || (( $(echo "$disk_usage > $threshold" | bc -l) )); then
    send_email
fi

echo "Script executed successfully."

