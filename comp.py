loop = 0
list = []
def out(int):
    return(int*2)
def return_binary(str):
    loop = 0
    lookup_table = {
        "imme": '00000000', "or": '01000000', "nand": '01000001', 
        "nor": '0100010', "and": '01000011', "sub": '01000101', 
        "mov": '10000000', "sreg0": '00000000', "sreg1": '00001000',
        "sreg2": '00010000', "sreg3": '00011000', "sreg4": '00100000',
        "sreg5": '00101000', "sin": '00110000', "lreg0": '00000000',
        "lreg1": '00000001', "lreg2": '00000010', "lreg3": '0000011',
        "lreg4": '0000100', "lreg5": '0000101', "lout": '00000110',
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
with open('open.txt', 'r') as file:
    for line in file:
        sav_ed = line.split('|')
        for item in sav_ed:
            list.append(return_binary(item))
with open('opened.txt', 'w') as fileout:
    for item in list:
        fileout.write(item)
