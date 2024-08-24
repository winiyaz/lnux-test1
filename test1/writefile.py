#!/usr/bin/env python

# Python file for writing fiels to disk and testing
# Taken from mistrk

import os
import json
import subprocess

# Check if the file exists
if not os.path.exists('tt.txt'):
    print('File not found - Creating and writing to the file')
    write_pnty = ["Panty Smell"]
    with open('tt.txt', 'w') as file:
        json.dump(write_pnty, file, indent=4)

# List file and display its contents
subprocess.run(["ls", "-al", "tt.txt"])
subprocess.run(["cat", "tt.txt"])
