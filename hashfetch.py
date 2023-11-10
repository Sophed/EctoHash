import hashlib
import os

os.chdir("./CLIENTS")

FILE_NAME = "Hashes.json"

with open('../' + FILE_NAME, 'w') as f:
            f.write('{\n')

for file in os.listdir("./"):
    try:
        currentFile = open(file, 'rb')
        hash = hashlib.md5(currentFile.read()).hexdigest()
        name = file.replace(".jar", "").replace(".disabled", "")
        
        print("Hashed " + name + " as " + hash)
        with open('../' + FILE_NAME, 'a') as f:
            f.write(f'   "{name}": "{hash}",\n')

    except:
        print("Skipping " + file + ", likely a directory.")
        continue

with open('../' + FILE_NAME, 'a') as f:
            f.write('}')

# remove trailing comma
with open('../' + FILE_NAME, 'r') as f:
    lines = f.readlines()
    with open('../' + FILE_NAME, 'w') as l:
        lines[-2] = lines[-2].replace(",", "")
        l.writelines(lines)

print("Written to " + FILE_NAME + ".")