# ex -4
import random


def encode(k):
    if len(k) < 3:
        return k[::-1]
    else:
        k = list(k)
        tmp = k[0]
        k[0] = k[-1]
        k[-1] = tmp
        for i in range(3):
            k.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
            k.insert(0, random.choice('abcdefghijklmnopqrstuvwxyz'))
        return ''.join(k)


def decode(k):
    if len(k) < 3:
        return k[::-1]
    else:
        k = list(k)
        for i in range(3):
            k.pop(0)
            k.pop(-1)
        tmp = k[0]
        k[0] = k[-1]
        k[-1] = tmp
        return ''.join(k)


inp = input("Enter your messsage: ")
enc = encode(inp)
print("Encoded message: ", enc)
dec = decode(enc)
print("Decoded message: ", dec)
