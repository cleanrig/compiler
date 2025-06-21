loop = 0
lo = 0
sel = 0
selo = 0
selt = 0
list = []
lineinfile = 0
def out(int):
    return(int*2)
def return_binary(str):
    loop = 0
    lookup_table = {
        "imme": '00000000', "or": '01000000', "nand": '01000001', 
        "nor": '0100010', "and": '01000011', "sub": '01000101', 
        "mov": '10000000', "lreg0": '00000000', "lreg1": '00001000',
        "lreg2": '00010000', "lreg3": '00011000', "lreg4": '00100000',
        "lreg5": '00101000', "lin": '00110000', "sreg0": '00000000',
        "sreg1": '00000001', "sreg2": '00000010', "sreg3": '0000011',
        "sreg4": '0000100', "sreg5": '0000101', "sout": '00000110',
        "never": '11000000', "equals0": '11000001', "lessthen": '110000010',
        "lstoe": '11000011', "always": '11000100', "notequals0": '11000101',
        "greatorequalto0": '11000110', "greaterthen0": '11000111',
        "lfromclock": '00000111'
    }
    if str in lookup_table:
        return lookup_table[str]
    if str.isdigit():
        return bin(int(str))[2:]
    return str
def mov_func(str):
    str = str.split('|')
    for token in str:
        if token == "mov":
            sel = 1
            se = token
        if token in lsregisters:
            selo = 1
            selosel = token
        if token in lsregisters and loop > 1:
            selt = 1
            seltsel = token
        if sel == 1 and selo == 1 and selt == 1:
            return(True)
with open('open.txt', 'r') as file:
    for line in file:
        lineinfile = lineinfile + 1
        save = ['sreg0', 'sreg1', 'sreg2', 'sreg3', 'sreg4', 'sreg5', 'sout']
        load = ['lreg0', 'lreg1', 'lreg2', 'lreg3', 'lreg4', 'lreg5', 'lin']
        sav_ed = line.split('|')
        if str(sav_ed[0]) == "mov":
            if str(sav_ed[1]) in load:
                if str(sav_ed[2]) in save:
                    int(return_binary(sav_ed[0]))
                    int1 = int(return_binary(sav_ed[0]), 2)
                    int2 = int(return_binary(sav_ed[1]), 2)
                    int3 = int(return_binary(sav_ed[2]), 2)
                    mvline = bin(int(int1) + int(int2) + int(int3))
                    list.append(bin(int(int1) + int(int2) + int(int3)))
                    print(mvline)
                else:
                    print("error in load register of line " + str(lineinfile) + ".")
            else:
                print("error in save register of line " + str(lineinfile) + ".")
        else:
            list.append(return_binary(item))
                

with open('opened.bin', 'w') as fileout:
    for item in list:
        fileout.write(item)
