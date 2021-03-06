f = open('BintoHex.h', mode='w')
f.write("//A C header converting 8-bit binary literal into hexadecimal literal. For some old C compiler \n")
f.write("#ifndef __BintoHex_h__\n#define __BintoHex_h__\n\n")
for HEX in range(0, 256):
    f.write(f"#define b{HEX:08b} {HEX:#04x} ")
    f.write('\n')
f.write("\n#endif //__BintoHex_h__")
f.close()
