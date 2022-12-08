from collections import defaultdict
with open("liste.txt") as f:
    liste = f.read().strip()
    
dict = defaultdict(int)
path = []

def day7(liste):
    for line in liste.split("\n"):
        if line.startswith("$ cd"):
            where = line.split()[2]
            #print(where)
            if where == "/":
                path.append("/")
            elif where == "..":
                path.pop()
            else:
                path.append(f"{path[-1]}{'/' if path[-1] != '/' else ''}{where}")
        if line[0].isnumeric():
            for p in path:
                print(int(line.split()[0]))
                dict[p] += int(line.split()[0])
    
    print(f"Part 1: {sum(s for s in dict.values() if s <= 100_000)}")
    print(f"Part 2: {min(s for s in dict.values() if s >= 30_000_000 - (70_000_000 - dict['/']))}")

day7(liste)