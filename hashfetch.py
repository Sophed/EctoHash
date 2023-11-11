import hashlib
import json
import os

'''
This script is used for generating the list of client hashes,
it searches through a directory and adds each file name & hash to
a JSON file which can then be used by the main program.
'''

OUTPUT_FILE = "Hashes.json"
CLIENTS_DIR = "./CLIENTS"
REMOVED_EXTENSIONS = [
    ".jar",
    ".disabled"
]
DATA = {}

os.chdir(CLIENTS_DIR)

# Add each file hash to the JSON file
for file in os.listdir("./"):

    # Skip directories
    if os.path.isdir(file):
        continue
    
    # Hash file
    currentFile = open(file, 'rb')
    hash = hashlib.md5(currentFile.read()).hexdigest()
    
    # Remove extensions
    for ext in REMOVED_EXTENSIONS:
        file = file.replace(ext, "")
    
    # Add to dict and log
    DATA[file] = hash
    print(f"Hashed {file} as {hash}")

# Load JSON from dict
with open('../' + OUTPUT_FILE, 'w') as f:
    json.dump(DATA, f, indent=4)

print("Written to " + OUTPUT_FILE + ".")