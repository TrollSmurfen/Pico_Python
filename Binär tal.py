from machine import Pin
from time import sleep
while True:
    for i in range(256):
        print(f'{i:08b}')
        sleep(0.5)