# Define a filename.
import extract 

filePathToCopy= extract.selectFile("kd")
specFile = open('specData.txt')
f1 = open('../test/output.py', 'a')

with specFile as f:
    contentOfSpect = f.readlines()

# Open the file as f.
# The function readlines() reads the file.
with open(filePathToCopy) as f:
    content = f.readlines()

# Show the file contents line by line.
# We added the comma to print single newlines and not double newlines.
# This is because the lines contain the newline character '\n'.
for line in content:
    if "dictOfDt = {}" in line:
        f1.write("dictOfDt = " + contentOfSpect[0] +'\n')
    else:
        f1.write(line)
