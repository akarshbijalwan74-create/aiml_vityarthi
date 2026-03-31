import datetime

def log_action(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {action}\n"
    with open("activity_log.txt", "a") as f:
        f.write(entry)
