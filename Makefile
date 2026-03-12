SHELL := /bin/bash
.SILENT:

.PHONY: all build run exec clean

all: build run

build:
	gcc main.c memory_utils.o -o main

run: exec

exec:
	if [ -z "$(SRNO)" ]; then echo "SRNO is required. Usage: make all SRNO=12345"; exit 1; fi; \
		./main $(SRNO)

clean:
	rm -f main