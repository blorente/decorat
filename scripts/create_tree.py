#!/usr/bin/python3

import subprocess
import json
import sys
from pathlib import Path

wiki_dir=Path(sys.argv[1])

def perr(msg, *args, **kwargs):
    print(msg, file=sys.stderr, *args, **kwargs)

def process_entry(entry, path_till_now, indentation):
    if entry["type"] == "directory":
        process_dir(entry, path_till_now, indentation)
    elif entry["type"] == "file":
        process_file(entry, path_till_now, indentation)

def process_file(file, path_till_now, indentation):
    filename = file["name"]
    filepath = path_till_now + "/" + filename
    print(" " * indentation + f"<li> <a href='{filename}'>{filename}</a></li>")

def process_dir(directory, path_till_now, indentation):
    dirname = directory["name"]
    current_path = path_till_now + "/" + dirname if path_till_now else dirname
    print(" " * indentation + f"<li>{dirname}/</li>")
    print(" " * indentation + f"<ul>")
    for entry in directory["contents"]:
        process_entry(entry, current_path, indentation + 2)
    print(" " * indentation + f"</ul>")


raw_data = subprocess.check_output(["tree", "-J", "."], cwd=wiki_dir).decode('utf-8')
data=json.loads(raw_data)
for entry in data:
    print(f"<ul>")
    process_entry(entry, "", 2) 
    print(f"</ul>")