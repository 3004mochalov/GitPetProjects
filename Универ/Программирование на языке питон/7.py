def main(d):
    A = d & 0b1111111111111111
    B = d & 0b1111111111110000000000000000
    C = d & 0b10000000000000000000000000000
    D = d & 0b100000000000000000000000000000
    E = d & 0b11000000000000000000000000000000
    A = A << 12
    B = B >> 16
    E = E >> 2
    D = D << 2
    C = C << 2
    return A | B | C | D | E

print(main(0x099ff53f))
print(main(0x66e33106))