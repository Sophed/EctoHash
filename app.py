import hashlib
import json
import os
import urllib.error
import urllib.request

import customtkinter


TARGET_REMOTE = "https://raw.githubusercontent.com/Sophed/EctoHash/master/Hashes.json"

print("Loading remote hashes...")
DETECTED_CLIENTS = {}
HASH_LIST = {}

try:
    with urllib.request.urlopen(TARGET_REMOTE) as url:
        HASH_LIST = json.load(url)
        print("Loaded hashes!")
        
except urllib.error.URLError:
    print("Failed to load remote hashes. If the issue persists, ensure you have an internet connection and check the GitHub repo.")
    exit(1)


def scan_file(hash, file) -> bool:
    if hash in HASH_LIST.values():
        # https://tenor.com/view/cat-what-is-happening-dim-dim-what-confused-gif-26463317
        DETECTED_CLIENTS[file] = list(HASH_LIST.keys())[list(HASH_LIST.values()).index(hash)]
        return True
    
    return False


def scan_dir(dir) -> None:
    for file in os.listdir(dir):
        if os.path.isdir(file):
            continue
        
        f = open(file, 'rb').read()
        hash = hashlib.md5(f).hexdigest()
        
        if scan_file(hash, file):
            print(f"Detected {DETECTED_CLIENTS[file]} in {file}")


def button_callback():
    dir = entry.get()
    
    if dir == "":
        label.configure(text="Please enter a directory to scan")
        return
    
    if not os.path.isdir(dir):
        label.configure(text="Invalid directory")
        return
    
    os.chdir(dir)
    scan_dir(dir)
    
    if len(DETECTED_CLIENTS) == 0:
        label.configure(text="Complete: No clients detected")
    else:
        label.configure(text="Complete: Detected clients, see console for details")

    
app = customtkinter.CTk()
app.title("EctoHash")
app.geometry("400x190")
app.resizable(False, False)

entry = customtkinter.CTkEntry(
    app,
    placeholder_text="Scan directory..."
)
entry.grid(
    row=0,
    column=0,
    padx=40,
    pady=24
)
entry.configure(
    width=320,
    height=34
)

button = customtkinter.CTkButton(
    app,
    text="Begin scan",
    command=button_callback
)
button.grid(
    row=1,
    column=0,
    padx=20,
    pady=0
)
button.configure(
    width=80,
    height=34
)
label = customtkinter.CTkLabel(
    app,
    text="~"
)
label.grid(
    row=2,
    column=0,
    padx=20,
    pady=20
)

app.mainloop()