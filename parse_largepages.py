import re
from collections import defaultdict

def process_log(in_file, out_file):
    
    adress_re = re.compile(r'0x[0-9a-fA-F]+')
    region_mask = ~((1 << 21) - 1)
    
    hits = defaultdict(int)

    with open(in_file, "r", encoding='utf-8', errors='ignore') as f_in:
        for line_text in f_in:
            if "L2 miss" not in line_text:
                continue

            line_parts = line_text.split()
            samples_count = 1
            try:
                samples_count = int(line_parts[1])
            except (IndexError, ValueError):
                pass

            for addr_match in adress_re.finditer(line_text):
                addr_int = int(addr_match.group(0), 16)
                region_addr = addr_int & region_mask
                hits[region_addr] += samples_count

    sorted_hits = sorted(hits.items(), key=lambda kv: kv[1], reverse=True)

    with open(out_file, "w") as f_out:
        for region, count in sorted_hits:
            f_out.write(f"0x{region:016x}\t{count}\n")


if __name__ == "__main__":
    process_log("largepages.txt", "largepages_parsed.txt")
