

filesystem = {}
p = ""
score = 0
dirs = []
with open("input", "r") as f:
    for x in f.read().splitlines():
        if (x[0] == "$"):
            cmd = x.split(" ")[1]
            if (cmd == "ls"):
                continue
            value = x.split(" ")[2]
            if (cmd == "cd" and value == "/"):
                p = "/"
                if (not filesystem.get("/")):
                    filesystem[p] = {}
            elif (cmd == "cd" and value == ".."):
                p = filesystem[p]["parent"]
            else:
                filesystem[p+value+"/"] = {"parent": p}
                p += value+"/"
        elif (x[0] != "d"):
            cmd = x.split(" ")
            if (filesystem.get(p).get("files")):
                if (int(cmd[0]) not in filesystem[p]["files"]):
                    filesystem[p]["files"].append(int(cmd[0]))
            else:
                filesystem[p]["files"] = [int(cmd[0]), ]

# Iterate over all paths in filesystem two times to calculate sum of every dir
for x, y in filesystem.items():
    dirsize = 0
    for q, z in filesystem.items():
        if (x in q and z.get("files")):
            dirsize += sum(z["files"])
    dirs.append(dirsize)
    if dirsize <= 100000:
        score += dirsize
pos = []
# Check difference in dir sizes to find possible ones to delete
for x in dirs:
    if (x >= (30000000 - (70000000 - max(dirs)))):
        pos.append(x)
print("#1:", score)
print("#2:", min(pos))
