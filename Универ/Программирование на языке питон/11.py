import struct
from enum import Enum


class Types(Enum):
    uint8 = '<B'
    uint16 = '<H'
    uint32 = '<I'
    uint64 = '<Q'
    int8 = '<b'
    int16 = '<h'
    int32 = '<i'
    int64 = '<q'
    float = '<f'
    double = '<d'
    char = '<c'


class BinaryReader:
    def __init__(self, source, offset):
        self.source = source
        self.offset = offset

    def read(self, pattern):
        value = struct.unpack_from(pattern.value, self.source, self.offset)
        self.offset += struct.calcsize(pattern.value)
        return value[0]


def read_a(reader: BinaryReader):
    a1 = reader.read(Types.int16)
    a2 = reader.read(Types.double)
    a3 = read_b(reader)
    a4 = reader.read(Types.double)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4)


def read_b(reader: BinaryReader):
    b1 = ""
    for _ in range(6):
        b1 += str(reader.read(Types.char))[2:-1]
    b2 = reader.read(Types.uint32)
    b3_size = reader.read(Types.uint32)
    b3_offset = reader.read(Types.uint16)
    b3 = []
    b3_reader = BinaryReader(reader.source, b3_offset)
    for _ in range(b3_size):
        b3.append(read_c(b3_reader))
    b4 = reader.read(Types.uint32)
    b5 = []
    b5_size = reader.read(Types.uint32)
    b5_offset = reader.read(Types.uint16)
    b5_reader = BinaryReader(reader.source, b5_offset)
    for _ in range(b5_size):
        b5.append(b5_reader.read(Types.int16))
    b6_offset = reader.read(Types.uint16)
    b6 = read_d(BinaryReader(reader.source, b6_offset))
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6)


def read_c(reader: BinaryReader):
    c1 = reader.read(Types.int16)
    c2 = reader.read(Types.uint8)
    c3 = []
    for _ in range(3):
        c3.append(reader.read(Types.uint16))
    c4 = reader.read(Types.float)
    c5 = reader.read(Types.uint32)
    c6 = reader.read(Types.uint32)
    c7 = []
    c7_size = reader.read(Types.uint16)
    c7_offset = reader.read(Types.uint16)
    c7_reader = BinaryReader(reader.source, c7_offset)
    for _ in range(c7_size):
        c7.append(c7_reader.read(Types.double))
    c8 = reader.read(Types.int8)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6, C7=c7, C8=c8)


def read_d(reader: BinaryReader):
    d1 = reader.read(Types.double)
    d2 = reader.read(Types.int64)
    d3 = reader.read(Types.float)
    return dict(D1=d1, D2=d2, D3=d3)


def main(data):
    reader = BinaryReader(data, offset=5)
    return read_a(reader)


print(main(b'WLXN}\x11\x9f\xfe\xf4s:\xfb\x04\xe5?unkpul\xb3\xe5\x00p\x02\x00\x00' b'\x00S\x00\xd6\\#\x8a\x04\x00\x00\x00\x87\x00\x8f\x00\xe0\xbd\x92\x9d\x8f' b'A\xb3?\x0c\xe9NM\x84\xe6\xdb\xbf\xdc*\xfch\xe2\xb4\xdd\xbf\xd8' b'\xd5\xd4\xfb\xa0\x00\xc0?T\xb7\xdb\x96\xd2\xbc\xd7\xbf\x92\xcc\xae\xe4\xe6' b"\x18\xb5L'u@\xa6\xbe7\xbf\xe6$\xfe^+r\x02\x003\x00\x90;\xcbC>C\x9a2" b'\xb2\xb2u\x13`?\xdc|\xb2X\x0c\xe9%\\\x02\x00C\x00\xf3\xa3\xd2\x1c\xb5\xfc' b'G\x96\xeb\xf0\xe7\xa64\xcb\x8a\xb6?F\xae\xbb\x84\xed\x1e#sM\x80\x13\xbf'))
