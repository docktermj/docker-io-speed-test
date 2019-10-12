#! /usr/bin/env python

import time

file_names = [
    "/inside/test-file.bin",
    "/outside/test-file.bin",
    "/outside/test-file.bin",
    "/inside/test-file.bin",
]

for file_name in file_names:
    start_time = time.time()

    byte_count = 0
    with open(file_name, "rb") as file:
        byte = file.read(1)
        while byte != "":
            byte_count += 1
            byte = file.read(1)

    elapsed_time = time.time() - start_time
    byte_rate = byte_count / elapsed_time
    print("elapsed time: {0}  bps: {1}  File: {2}".format(elapsed_time, byte_rate, file_name))
