#!/bin/python
# Take "<raw>": "<translated>" (and optional comments) as input, copy typey type lesson format to clipboard.
import subprocess
import sys
import re
data=""
regex=re.compile(r"\s*'(.+)':\s*'(.+)',?\s*(?:#.*)?$")
for line in sys.stdin.readlines():
	line=line.strip()
	match=regex.fullmatch(line)
	if match:
		raw, translated=match[1], match[2]
		data+=f"{translated}\t{raw}\n"

if data:
	subprocess.run(["xclip", "-selection", "clipboard"], input=data.encode("u8"))
else:
	print("No data!")
