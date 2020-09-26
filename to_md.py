#!/usr/bin/python3

# Converting Jupyter Notebook files in directories to markdown.
from os import listdir
from os import system

files = listdir().copy()

if 'markdown' not in files:
    print('markdown folder not found.')
    cmd = 'mkdir markdown'
    system(cmd)
else:
    print('markdown folder exists.\n--')

notes = list(filter(lambda x : x.endswith('.ipynb'), files))

print('-- Notes to be converted to markdown:')
print(notes)

for note in notes:
    command = 'jupyter nbconvert --output-dir=\'./markdown\' --to markdown \'' + note + '\''
    print('Current command:', command)
    system(command)

print('Conversion complete.')
