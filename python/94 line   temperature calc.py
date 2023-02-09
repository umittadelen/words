import os
def from_c():
    if newtemp == temp:
        return firstemp
    if newtemp == "F":
        return firstemp*1.8+32
    if newtemp == "K":
        return firstemp+273.15
    if newtemp == "Ra":
        return firstemp+273.15*1.8
    if newtemp == "Re":
        return firstemp*0.8
def from_f():
    if newtemp == temp:
        return firstemp
    if newtemp == "C":
        return (firstemp-32)/1.8
    if newtemp == "K":
        return (firstemp+459.67)/1.8
    if newtemp == "Ra":
        return firstemp+459.67
    if newtemp == "Re":
        return (firstemp-32)*4/9
def from_k():
    if newtemp == temp:
        return firstemp
    if newtemp == "C":
        return firstemp-273.15
    if newtemp == "F":
        return firstemp*1.8-459.67
    if newtemp == "Ra":
        return firstemp*1.8
    if newtemp == "Re":
        return (firstemp-273.15)*0.8
def from_ra():
    if newtemp == temp:
        return firstemp
    if newtemp == "C":
        return (firstemp-491.67)/1.8
    if newtemp == "F":
        return firstemp-459.67
    if newtemp == "K":
        return firstemp/1.8
    if newtemp == "Re":
        return (firstemp-491.67)*4/9
def from_re():
    if newtemp == temp:
        return firstemp
    if newtemp == "C":
        return firstemp/0.8
    if newtemp == "F":
        return firstemp*9/4+32
    if newtemp == "K":
        return firstemp*1.25+273.15
    if newtemp == "Ra":
        return firstemp*9/4+491.67
loop = 1
while loop == 1:
    try:
        temp = input("enter type (from C F K Ra Re   exit) > °")
        firstemp = int(input("enter temperature > "))
        newtemp = input("enter (to C F K Ra Re) > °")
    except:
        print("invalid type...")

    if temp == "C":
        print(from_c(),"\n")
        input()
        os.system("cls")

    elif temp == "F":
        print(from_f(),"\n")
        input()
        os.system("cls")

    elif temp == "K":
        print(from_k(),"\n")
        input()
        os.system("cls")

    elif temp == "Ra":
        print(from_ra(),"\n")
        input()
        os.system("cls")

    elif temp == "Re":
        print(from_re(),"\n")
        input()
        os.system("cls")
    
    elif temp =="exit" or newtemp =="exit" or firstemp =="exit":
        loop = 0
os.system("exit")
