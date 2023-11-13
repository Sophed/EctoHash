import json
from hashlib import md5
from pathlib import Path

'''
This script is used for generating the list of client hashes,
it searches through a directory and adds each file name & hash to
a JSON file which can then be used by the main program.
'''

HASH_FILE = 'Hashes.json'
CLIENTS_DIR = Path('./CLIENTS')

VALID_EXTENSIONS = {
    '*.jar', 
    '*.disabled'
}

files = []
for ext in VALID_EXTENSIONS:
    files.extend(CLIENTS_DIR.glob(ext))
    
if len(files) == 0:
    print(f'''
          No files matching the valid extensions were found.''')
    print(f'Clients directory checked: {CLIENTS_DIR}.')
    print(f'Valid extensions provided: {VALID_EXTENSIONS}.')
    exit(1)
    
    
hashes = {}
for file in files:
    
    with open(file, 'rb') as f:
        file_hash = md5(f.read()).hexdigest()
        hashes.update({file.name: file_hash})
        print(f'Hashed {file.name} as {file_hash}')

with open(HASH_FILE, 'w') as f:
    json.dump(hashes, f, indent=4)
    
print(f'Written to {HASH_FILE}.')