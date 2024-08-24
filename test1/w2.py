#!/usr/bin/env python

# Python file for writing files to disk and testing
# Taken from mistrk

import os
import subprocess

# Check if the file exists
if not os.path.exists('ttw2.txt'):
    print('File not found - Creating and writing to the file')
    write_pnty = ["Panty Smells", "FartNose"]
    with open('ttw2.txt', 'w') as file:
        for item in write_pnty:
            file.write(item + '\n')

# List file and display its contents
subprocess.run(["ls", "-al", "tt.txt"])
subprocess.run(["cat", "tt.txt"])
