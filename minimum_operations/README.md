## Minimum Operations

a Python function that counts minimum operations to duplicate the character H
till it reach the n number

## Usage

carrie@ubuntu:~/minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = **import**('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/minoperations$

###  Output

carrie@ubuntu:~/0x03-minoperations$ ./0-main.py

Min number of operations to reach 4 characters: 4

Min number of operations to reach 12 characters: 7
