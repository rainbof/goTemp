#!/usr/bin/python
import time
import struct

ldusb = file("/dev/ldusb0")

time.sleep(0.5)

# for n in range(10):
while True:
    # time.sleep(0.5)
    pkt = ldusb.read(8)
    parsed_pkt = list(struct.unpack("<BBHHH", pkt))
    num_samples = parsed_pkt.pop(0)
    seqno = parsed_pkt.pop(0)
    for sample in range(num_samples):
        print seqno+sample, parsed_pkt[sample]/100.0
    # time.sleep(0.5)
