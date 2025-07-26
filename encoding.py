a = input("Enter the message:")
apl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = int(input("Enter the key:"))
mode = input("Type 'encode' or 'decode': ").lower()

for i in range(len(a)):
    char = a[i]
    if char.lower() in apl.lower():
        index = 0
        for j in apl:
            if char.lower() == j.lower():
                break
            index += 1

        if mode == "decode":
            shift = (index - key) % 26
        else: 
            shift = (index + key) % 26

        if char.isupper():
            print(apl[shift], end="")
        else:
            print(apl[shift].lower(), end="")
    else:
        print(char, end="") 