import os
import psutil

log_path = "C:\\Users\\Public\\keylog.txt"
warning = False

if os.path.exists(log_path):
    print(f"Suspected logs file: {log_path}")
    warning = True

for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        if 'python' in proc.info['name'].lower() or 'python' in ' '.join(proc.info['cmdline']).lower():
            print(f"Suspected keylogger process: PID {proc.info['pid']} CMD {proc.info['cmdline']}")
            warning = True
    except Exception:
        continue

if not warning:
    print("No obvious keylogger detected.")
