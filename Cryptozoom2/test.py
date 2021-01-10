#!/usr/bin/env python3
text = 'Bro... Some cool ass text coming at you.'
index = 0
try:
    while True:
        print (text[index:])
        index += 1
    if index > len(text):
        index = 0
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

