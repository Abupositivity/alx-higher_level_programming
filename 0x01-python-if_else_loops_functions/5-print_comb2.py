#!/usr/bin/python3
'''prints number from 0-99'''
for num in range (0, 99):
    print('{:02d}, '.format(num), end='')
print('99')
