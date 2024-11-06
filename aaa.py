import os



import_statments = []

with open ("TextConvoNet.py", "r") as f:
    for line in f:
        if line.startswith("import"):
           import_statments.append(line)
        elif line.startswith("from"):
            import_statments.append(line)


import_statments = list(set(import_statments))


import_statments.sort()

with open("import_statements.txt","w") as out:
    for line in import_statments:
        out.write(line)