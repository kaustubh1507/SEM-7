import pandas as pd
import time

# Event correlation rules
CORRELATION_RULES = {
    "failed_login": {
        "pattern": r"failed login",
        "threshold": 5,
        "description": "Multiple failed login attempts detected."
    },
    "successful_login": {
        "pattern": r"successful login",
        "description": "Successful login detected."
    },
}

# Function to read logs from a file
def read_logs(log_file):
    try:
        with open(log_file, 'r') as file:
            return file.readlines()
    except Exception as e:
        print(f"Error reading log file: {e}")
        return []

# Function to correlate events
def correlate_events(logs):
    log_data = []

    for log in logs:
        log_data.append({'log': log.strip()})  # Append only the log text to the list

    # Check if there are logs to process
    if not log_data:
        print("No logs to process.")
        return

    # Create a DataFrame from the log data
    df = pd.DataFrame(log_data)

    # Correlate events based on rules
    for rule_name, rule in CORRELATION_RULES.items():
        pattern = rule["pattern"]
        if 'threshold' in rule:
            # Check for threshold-based correlation
            count = df['log'].str.contains(pattern, na=False).sum()  # Ensure to handle NaN values
            if count >= rule["threshold"]:
                print(f"[ALERT] {rule['description']} (Count: {count})")
        else:
            # Check for single occurrence correlation
            if df['log'].str.contains(pattern, na=False).any():  # Ensure to handle NaN values
                print(f"[INFO] {rule['description']}")

# Main function
if __name__ == "__main__":
    log_file_path = 'system.log'  # Change this to your log file path

    while True:
        logs = read_logs(log_file_path)
        correlate_events(logs)
        time.sleep(10)  # Wait for a while before reading logs again
