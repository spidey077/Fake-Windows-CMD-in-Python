import time
import random
import os

# ================= STATE =================
current_dir = "C:\\Users\\Imdadullah"
history = []
color = "07"

fake_fs = {
    "C:\\Users\\Imdadullah": ["Documents", "Downloads", "notes.txt"],
    "C:\\Users\\Imdadullah\\Documents": ["project.txt"],
    "C:\\Users\\Imdadullah\\Downloads": []
}

files_content = {
    "notes.txt": "Remember to submit AI assignment.\nPractice DSA.\n",
    "project.txt": "Final year project ideas:\n- Network simulator\n- Fake CMD in Python\n"
}

tasks = [
    {"pid": 1024, "name": "explorer.exe"},
    {"pid": 2211, "name": "chrome.exe"},
    {"pid": 3320, "name": "python.exe"}
]

# ================= HELPERS =================
def slow_print(text, delay=0.02):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

# ================= COMMANDS =================
def cmd_exit(args):
    print("Exiting mock CMD...")
    return False

def cmd_ver(args):
    print("Microsoft Windows [Version 15.0.26000]")

def cmd_whoami(args):
    print("desktop-imdadullah\\imdadullah")

def cmd_date(args):
    print(time.strftime("%A %Y-%m-%d"))

def cmd_time(args):
    print(time.strftime("%H:%M:%S"))

def cmd_cls(args):
    os.system("cls" if os.name == "nt" else "clear")

def cmd_echo(args):
    print(" ".join(args))

def cmd_ipconfig(args):
    print("\nWindows IP Configuration\n")
    print("IPv4 Address . . . . . . : 192.168.100.7")
    print("Subnet Mask  . . . . . . : 255.255.255.0")
    print("Default Gateway . . . .  : 192.168.100.1\n")

def cmd_ping(args):
    target = args[0] if args else "127.0.0.1"
    print(f"\nPinging {target} with 32 bytes of data:")
    for _ in range(4):
        time.sleep(0.4)
        print(f"Reply from {target}: bytes=32 time={random.randint(5,40)}ms TTL=54")
    print("\nPackets: Sent = 4, Received = 4, Lost = 0 (0% loss)\n")

def cmd_tracert(args):
    target = args[0] if args else "google.com"
    print(f"\nTracing route to {target}\n")
    hops = ["192.168.100.1", "10.20.1.1", "150.222.7.97", "216.198.79.131"]
    for i, hop in enumerate(hops, 1):
        time.sleep(0.3)
        print(f"{i}\t{random.randint(5,30)} ms\t{hop}")
    print("\nTrace complete.\n")

def cmd_arp(args):
    print("\nInternet Address      Physical Address      Type")
    print("192.168.100.1         e8-a6-60-b5-39-52     dynamic\n")

def cmd_netstat(args):
    print("\nActive Connections")
    print("TCP    192.168.100.7:52344   142.250.183.78:443   ESTABLISHED\n")

def cmd_dir(args):
    print(f"\n Directory of {current_dir}\n")
    for item in fake_fs.get(current_dir, []):
        print(f"    {item}")
    print()

def cmd_cd(args):
    global current_dir
    if not args:
        print(current_dir)
        return

    target = args[0]
    if target == "..":
        if "\\" in current_dir:
            current_dir = "\\".join(current_dir.split("\\")[:-1])
        return

    new_path = f"{current_dir}\\{target}"
    if new_path in fake_fs:
        current_dir = new_path
    else:
        print("The system cannot find the path specified.")

def cmd_type(args):
    if not args:
        print("File name required.")
        return
    file = args[0]
    if file in files_content:
        print()
        print(files_content[file])
    else:
        print("The system cannot find the file specified.")

def cmd_del(args):
    if not args:
        print("File name required.")
        return
    file = args[0]
    if file in fake_fs.get(current_dir, []):
        fake_fs[current_dir].remove(file)
        files_content.pop(file, None)
        print("File deleted.")
    else:
        print("File not found.")

def cmd_mkdir(args):
    if not args:
        print("Directory name required.")
        return
    name = args[0]
    path = f"{current_dir}\\{name}"
    fake_fs[path] = []
    fake_fs[current_dir].append(name)

def cmd_rmdir(args):
    if not args:
        print("Directory name required.")
        return
    name = args[0]
    path = f"{current_dir}\\{name}"
    if path in fake_fs and not fake_fs[path]:
        fake_fs.pop(path)
        fake_fs[current_dir].remove(name)
        print("Directory removed.")
    else:
        print("Directory not empty or not found.")

def cmd_tasklist(args):
    print("\nImage Name         PID")
    for t in tasks:
        print(f"{t['name']:<18}{t['pid']}")
    print()

def cmd_taskkill(args):
    if len(args) < 2 or args[0] != "/pid":
        print("Usage: taskkill /pid <id>")
        return
    pid = int(args[1])
    for t in tasks:
        if t["pid"] == pid:
            tasks.remove(t)
            print(f"Process {pid} terminated.")
            return
    print("Process not found.")

def cmd_systeminfo(args):
    print("\nOS Name: Microsoft Windows 15 Pro")
    print("System Type: x64-based PC")
    print("Processor: Intel(R) Core(TM) i7")
    print("Installed Memory: 16 GB\n")

def cmd_color(args):
    global color
    if args:
        color = args[0]
    print(f"Color set to {color}")

def cmd_history(args):
    print()
    for i, h in enumerate(history, 1):
        print(f"{i}: {h}")
    print()

def cmd_help(args):
    print("\nAvailable commands:")
    for c in sorted(commands.keys()):
        print(" ", c)
    print()

# ================= DISPATCH =================
commands = {
    "exit": cmd_exit,
    "ver": cmd_ver,
    "whoami": cmd_whoami,
    "date": cmd_date,
    "time": cmd_time,
    "cls": cmd_cls,
    "echo": cmd_echo,
    "ipconfig": cmd_ipconfig,
    "ping": cmd_ping,
    "tracert": cmd_tracert,
    "arp": cmd_arp,
    "netstat": cmd_netstat,
    "dir": cmd_dir,
    "cd": cmd_cd,
    "type": cmd_type,
    "del": cmd_del,
    "mkdir": cmd_mkdir,
    "rmdir": cmd_rmdir,
    "tasklist": cmd_tasklist,
    "taskkill": cmd_taskkill,
    "systeminfo": cmd_systeminfo,
    "color": cmd_color,
    "history": cmd_history,
    "help": cmd_help
}

# ================= MAIN LOOP =================
def mock_cmd():
    slow_print("Microsoft Windows 15 Pro")
    print("(c) Microsoft Corporation. All rights reserved.\n")

    running = True
    while running:
        raw = input(f"{current_dir}> ").strip()
        if not raw:
            continue

        history.append(raw)
        parts = raw.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd in commands:
            result = commands[cmd](args)
            if result is False:
                running = False
        else:
            print(f"'{cmd}' is not recognized as an internal or external command.\n")

mock_cmd()
