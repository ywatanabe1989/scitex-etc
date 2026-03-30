#!/usr/bin/env python3
# File: src/scitex_etc/wait_key.py

import multiprocessing
import time

import readchar


def wait_key(p):
    key = "x"
    while key != "q":
        key = readchar.readchar()
        print(key)
    print("q was pressed.")
    p.terminate()


def count():
    counter = 0
    while True:
        print(counter)
        time.sleep(1)
        counter += 1


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=count)

    p1.start()
    wait_key(p1)
    print("aaa")

# EOF
