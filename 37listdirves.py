import os, re
x = re.findall(r"[A-Z]+:.*$",os.popen("mountvol /").read(),re.MULTILINE)
for y in x:
    print(y)