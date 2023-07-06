import lzw, json, binascii
from machine import Pin, ADC
from kongduino import *

randomBuff = bytearray(128)
randomIndex = 0
hw_trng(randomBuff)

def getRandomByte():
    global randomIndex, randomBuff
    if randomIndex > 126:
        hw_trng(randomBuff)
        randomIndex = 0
    x = randomBuff[randomIndex]
    randomIndex += 1
    return x

def getRandomWord():
    global randomIndex, randomBuff
    if randomIndex == 128:
        hw_trng(randomBuff)
        randomIndex = 0
    x = randomBuff[randomIndex] << 8 | randomBuff[randomIndex+1]
    randomIndex += 2
    return x

temp = (getRandomByte() % 130) / 10.0 + 12
hum = (getRandomByte() /10.0) + 30
press = getRandomWord() % 120 + 900
a=bytearray(4)
for i in range(0, 4):
    a[i] = getRandomByte()
UUID = binascii.hexlify(a).decode() 
packet = {}
packet['temp'] = temp
packet['hum'] = hum
packet['press'] = press
packet['msgID'] = UUID

msg = json.dumps(packet).replace(' ','')
print(msg)
pkt = lzw.compress(msg)
print(pkt)
s1 = len(pkt)
s0 = len(msg)
ratio = (1 - (s1 / s0))*100
print("Compression: {} vs {} bytes, ie {:.2f}%".format(s1, s0, ratio))

pIV = bytearray(16)
for i in range(0, 16):
    pIV[i] = getRandomByte()
pKey = bytearray(32)
for i in range(0, 32):
    pKey[i] = getRandomByte()
print("> Key")
hexdump(pKey)
print("> IV")
hexdump(pIV)
print("> Plaintext")
hexdump(pkt)
result = encryptAES_CBC(msg, pKey, pIV)
print("> Ciphertext")
hexdump(msg)
result = decryptAES_CBC(msg, pKey, pIV)
print("> Deciphered")
print(msg)
