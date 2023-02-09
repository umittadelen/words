val = 0
characters = ""
a = True
while a == True:
    if val >= 55296:
        a = False
    else:
        print(f"{chr(val)} = ASCII {val}")
        characters = characters + chr(val)
    val = val + 1

print(characters)
print(f"ඞ = {ord('ඞ')}")
input()