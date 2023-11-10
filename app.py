import urllib.request
import customtkinter
import hashlib
import json
import os

#FILE_NAME = "Hashes.json"
SKIP_DIRS = [".index", ".git"]
TARGET_REMOTE = "https://raw.githubusercontent.com/Sophed/EctoHash/master/Hashes.json"

print("Loading remote hashes...")
HASH_LIST = {}

try:
    with urllib.request.urlopen(TARGET_REMOTE) as url:
        HASH_LIST = json.load(url)
        print("Loaded hashes!")
except:
    print("Failed to load remote hashes. If the issue persists, ensure you have an internet connection and check the GitHub repo.")
    exit(1)

'''
with open(FILE_NAME, 'r') as f:
    HASH_LIST = json.load(f)
'''

# Dict of files that match a known client hash
DETECTED_CLIENTS = {}


targetDir = ""

# Check if the hash is in the list of known hashes
def checkFile(hash, file):
    if hash in HASH_LIST.values():
        DETECTED_CLIENTS[file] = list(HASH_LIST.keys())[list(HASH_LIST.values()).index(hash)]
        return True
    return False

def checkDir(dir):
    for file in os.listdir(dir):
        if file in SKIP_DIRS or os.path.isdir(file):
            continue
        currentFile = open(file, 'rb')
        hash = hashlib.md5(currentFile.read()).hexdigest()
        if checkFile(hash, file) == True:
            print("Detected " + DETECTED_CLIENTS[file] + " in " + file)

def button_callback():
    dir = entry.get()
    if dir == "":
        label.configure(text="Please enter a directory to scan")
        return
    if os.path.isdir(dir) == False:
        label.configure(text="Invalid directory")
        return
    os.chdir(dir)
    checkDir(dir)
    if len(DETECTED_CLIENTS) == 0:
        label.configure(text="Complete: No clients detected")
    else:
        label.configure(text="Complete: Detected clients, see console for details")

    
app = customtkinter.CTk()
app.title("EctoHash")
app.geometry("400x190")

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