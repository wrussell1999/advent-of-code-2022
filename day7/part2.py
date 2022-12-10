TOTAL_DISK_SPACE = 70000000
UPDATE = 30000000

with open('input.txt') as f:
    lines = f.readlines()

    dirs = {}
    counter = 0
    current_dir = ""
    parent_dir = []
    for line in lines:
        chunks = line.split()
        if chunks[0] == "$":
            if chunks[1] == "cd" and chunks[2] != "..":
                
                parent_dir.append(chunks[2])
                current_dir = '_'.join(parent_dir)
                dirs[current_dir] = {
                    "size": 0,
                    "files": [],
                    "dirs": []
                }
                counter += 1
            elif chunks[1] == "cd" and chunks[2] == "..":
                parent_dir.pop()
        elif chunks[0] == "dir":
            dirs[current_dir]["dirs"].append(f"{'_'.join(parent_dir)}_{chunks[1]}")
        else:
            dirs[current_dir]["size"] += int(chunks[0])
            dirs[current_dir]["files"].append(int(chunks[0]))
    sizes = {}

    def sum_directory(dir):
        sum = 0
        if len(dirs[dir]["dirs"]) > 0:
            for sub_dir in dirs[dir]["dirs"]:
                sum += sum_directory(sub_dir)
        sum += dirs[dir]["size"]
        sizes[sum] = dir
        return sum
    root_size = sum_directory("/")
    
    diff = {}
    space_free = TOTAL_DISK_SPACE - root_size
    space_needed = UPDATE - space_free
    for size in sizes:
        freed_space = size- space_needed
        if freed_space >= 0:
            diff[freed_space] = {
                "size": size,
                "dir": sizes[size]
            }

    print(diff[min(diff)]["size"])
