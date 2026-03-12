#include "memory_utils.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <5-digit SRNO>\n", argv[0]);
        return 1;
    }

    int srno = atoi(argv[1]);

    // Initialize memory
    memory_init(srno);
    // // Do not make changes above

    // int pages = 474;
    // FILE *huge_pages = fopen("hugepages.txt", "r");

    // char line[128];
    // while (fgets(line, sizeof(line), huge_pages)) {
    //     // Example line format: "0x000070aad9400000    788"
    //     char addr_str[32];
    //     if (sscanf(line, "%31s", addr_str) == 1) {
    //         // Convert hex string to 64-bit integer
    //         long addr = strtoull(addr_str, NULL, 0);
    //         // printf("%s\n", addr_str);
    //         allocate_huge_page(addr);
    //     }
    //     if(!pages){
    //         break;
    //     }
    //     pages--;
    // }
    
    // Make changes here to allocate huge pages to specific addresses
    // You can call allocate_huge_page with the desired addresses or write your own logic
    // Example usage for allocating huge page at address addr
    // long addr = strtol("0x000070aad9400000", NULL, 16);
    // allocate_huge_page(addr);

    // Do not make changes below
    // Benchmark memory
    memory_benchmark();

    return 0;
}