import random,os
os.system("cls")

while True:
    lines = []
    with open('C:/Users/umtaa005/Desktop/words.txt') as f:
        lines = f.readlines()
        
    for i in range(0,len(lines)):
        lines[i] = lines[i].replace("\n","")

    for prt in range(0,4):
        for lin in range(0,4):
            for wrd in range(0,4):
                print(random.choice(lines),end=" ")
            print("")
        print("")

    input()
    os.system("cls")