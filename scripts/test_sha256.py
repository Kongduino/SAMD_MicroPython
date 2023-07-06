from kongduino import *

buf = bytearray(128)
hw_trng(buf)
hexdump(buf)
myHash = bytearray(32)
result = hw_sha256(buf, myHash)
hexdump(myHash)

buf = b"qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@"
hexdump(buf)
result = hw_sha256(buf, myHash)
hexdump(myHash)
