#!/usr/bin/python3
from dis import dis
with open('hidden_4.pyc', 'rb') as file:
    bytecode = file.read()

for str in dir(bytecode):
    if (str.startswith('__')):
        continue
    print(str)
