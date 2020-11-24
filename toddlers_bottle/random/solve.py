#!/usr/bin/env python3 
import pwn
import logging
#pwn.context.log_level = logging.ERROR

s = pwn.ssh("random", "pwnable.kr", 2222, "guest", keyfile="")
#sh = s.shell()
p = s.process(["./random"])
#p = pwn.process(["nc", "pwnable.kr", ""])
#p = pwn.process(["./random"])

p.sendline(str(1804289383 ^ 0xdeadbeef))
p.readline()
print(p.readline().decode("utf-8"))
