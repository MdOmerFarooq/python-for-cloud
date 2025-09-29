# File operations

File operations in Python are all about creating, reading, writing, and managing files. They’re very useful because almost every program interacts with files at some point (logs, configs, data, etc.). <br>

Python provides the built-in open() function to work with files.

## Syntax
file = open("filename.txt", "mode")

### Common Modes:

"r" → read (default, error if file doesn’t exist)

"w" → write (creates new or overwrites existing file)

"a" → append (adds to end of file, doesn’t erase content)

"x" → create (fails if file exists)

"b" → binary mode (e.g., "rb", "wb")

"t" → text mode (default, e.g., "rt", "wt")

## Using with Statement

You don’t need to call close() manually. It auto-closes after the block.

with open("example.txt", "r") as f:
    data = f.read()
    print(data)

--> file is closed automatically here