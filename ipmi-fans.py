#!/usr/bin/env python3

from sys import argv, exit
from os  import system

command = "ipmitool -U root -P calvin -H 172.30.42.220 raw 0x30 0x30 0x02 0xff %s"

if len(argv) == 2 and argv[1].isdigit() and int(argv[1]) in range(-1, 101):
    hex_value = hex(int(argv[1]))
elif len(argv) == 2 and argv[1] == "auto":
    command = "ipmitool -U root -P calvin -H 172.30.42.220 raw 0x30 0x30 0x01 %s"
    hex_value = 0x01
elif len(argv) == 2 and argv[1] == "manual":
    command = "ipmitool -U root -P calvin -H 172.30.42.220 raw 0x30 0x30 0x01 %s"
    hex_value = 0x00
else:
    print("Error: bad input, exiting.")
    exit(42)

print(command % hex_value)
system(command % hex_value)

