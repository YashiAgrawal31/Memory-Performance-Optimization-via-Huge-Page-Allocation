def get_data(file_path):
    ordered_keys = []
    data_map = {}
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            parts = line.split()
            if len(parts) >= 2:
                addr = parts[0]
                try:
                    count = int(parts[1])
                    ordered_keys.append(addr)
                    data_map[addr] = count
                except ValueError:
                    pass
                    
    return ordered_keys, data_map

input_file = 'smallpages_parsed.txt'
output_file = 'hugepages.txt'
max = 12

keys, counts = get_data(input_file)

with open(output_file, "w") as f:
    for addr_key in keys:
        if counts.get(addr_key, 0) >= max:
            addr_as_int = int(addr_key, 16)
            f.write(f"{addr_as_int}\n")
