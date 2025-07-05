def opcode(string):
    lookup_table = {
        "imme": '00000000', "or": '01000000', "nand": '01000001', 
        "nor": '0100010', "and": '01000011', "sub": '01000101', 
        "mov": '10000000', "lreg0": '00000000', "lreg1": '00001000',
        "lreg2": '00010000', "lreg3": '00011000', "lreg4": '00100000',
        "lreg5": '00101000', "lin": '00110000', "sreg0": '00000000',
        "sreg1": '00000001', "sreg2": '00000010', "sreg3": '00000011',
        "sreg4": '0000100', "sreg5": '0000101', "sout": '00000110',
        "never": '11000000', "equals0": '11000001', "lessthen": '110000010',
        "lstoe": '11000011', "always": '11000100', "notequals0": '11000101',
        "greatorequalto0": '11000110', "greaterthen0": '11000111',
        "lfromclock": '00000111'
    }
    if string in lookup_table:
        saveout = (lookup_table[string])
        return(saveout)
    else:
        print("Binary")
        return(bin(int(string)))
def add_binary(byte1, byte2):
    b1 = int(byte1)
    b2 = int(byte2)
    b3 = str(int(b1 + b2))
    print(b1)
    return(b3)
def leng(string):
    if len(string) == 8:
        return(True)
    else:
        return(False)
chose = open("program.txt", "r")
parts = open("program.bin", "w")

for line in chose:
    line = line.strip("\n")
    lineparts = line.split("|")
    print(lineparts)
    if lineparts[0] == "imme":
        with open("program.bin", "a") as parts:
            parts.write(str(int(lineparts[1])))
            parts.write("\n")
    else:
        with open("program.bin", "a") as parts:
            lineparts = line.split("|")
            if lineparts[0] == "mov":
                print("123")
                suma = add_binary(opcode(lineparts[1]), opcode(lineparts[2]))
                sumb = (add_binary(opcode(lineparts[0]), suma))
                print(suma)
                print(sumb)
                parts.write(sumb)
                parts.write("\n")
            else:
                for item in lineparts:
                    parts.write(bin(int(opcode(item))))
                    parts.write("\n")

with open('opened.bin', 'w') as fileout:
    for item in list:
        fileout.write(item)
