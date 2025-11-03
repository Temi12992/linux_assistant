import tkinter as tk
import tkinter.messagebox as mbox
import getpass
from datetime import datetime
import os
import sys
import time

# === 1. Show popup immediately when you run this file ===
root = tk.Tk()
root.withdraw()

username = getpass.getuser()
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

mbox.showinfo("Current User", f"User: {username}\nDate: {current_date}")
root.destroy()

# === 2. Setup autostart ===
home = os.path.expanduser("~")
autostart_dir = os.path.join(home, ".config", "autostart")
os.makedirs(autostart_dir, exist_ok=True)

script_path = os.path.join(home, "Script_file.py")  # <-- YOUR FILE NAME
desktop_file = os.path.join(autostart_dir, "show_user.desktop")
python_path = sys.executable  # full path to Python (e.g., /usr/bin/python3)

# === 3. Create or update the startup script ===
startup_script = """import tkinter as tk
import tkinter.messagebox as mbox
import getpass
from datetime import datetime
import os
import time

# Wait for the desktop environment to fully load
time.sleep(10)
os.environ["DISPLAY"] = ":0"

root = tk.Tk()
root.withdraw()
username = getpass.getuser()
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
mbox.showinfo("Current User", f"User: {username}\\nDate: {current_date}")
root.destroy()
"""

# Save (or overwrite) your startup file
with open(script_path, "w") as s:
    s.write(startup_script)
os.chmod(script_path, 0o755)

# === 4. Create the .desktop autostart entry ===
desktop_content = f"""[Desktop Entry]
Type=Application
Exec={python_path} {script_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Show User on Startup
Comment=Shows current user when computer starts
Terminal=false
"""

with open(desktop_file, "w") as f:
    f.write(desktop_content)
os.chmod(desktop_file, 0o755)

print(f"✅ Autostart entry added: {desktop_file}")
print(f"✅ Script configured at: {script_path}")
print("It will show your username and date each time you log in!")
