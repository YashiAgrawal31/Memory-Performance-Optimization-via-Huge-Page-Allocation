#ifndef MEMORY_UTILS_H
#define MEMORY_UTILS_H

void memory_init(int srno);
void memory_benchmark();
void allocate_huge_page(unsigned long addr); // Expose the huge page allocation function

#endif // MEMORY_UTILS_H
