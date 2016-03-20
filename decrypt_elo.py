#!/usr/bin/env python

import re

def decrypt(row, cipher):
    plain = ""
    seed = ((row * 0x1E2F) + 0xFE64) & 0xFFFFFFFF
    for byte in bytes.fromhex(cipher):
        mask = (seed >> 8) & 0xFF
        plain += chr(byte ^ mask)
        seed = (((seed + byte) * 0x0E6C9AA0) + 0x196AAA91) & 0xFFFFFFFF
    plain = re.sub("[^0-9]", "", plain)
    return plain

def main():
    infile = open("siste.txt", "r", encoding="cp865")
    outfile = open("output.txt", "w", encoding="cp865")
    infile.readline()
    row = 0
    for line in infile.readlines():
        fields = line.split(";")
        fields[11] = decrypt(row, fields[11])
        outfile.write(";".join(fields))
        row += 1
    outfile.close()
    infile.close()

main()
