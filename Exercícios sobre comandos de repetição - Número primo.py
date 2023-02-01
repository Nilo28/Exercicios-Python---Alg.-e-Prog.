list = [0,12,34,46,75,99,]
print(len(list))

for a in range(0, len(list)):
    if list[a] > -1 and list[a] < 26:
        print("\nMenor que 26", list[a])
    elif list[a] > 25 and list[a] < 51:
        print("\nMenor que 51", list[a])
    elif list[a] > 50 and list[a] < 76:
        print("\nMenor que 76", list[a])
    elif list[a] > 75 and list[a] < 101:
        print("\nMenor que 101", list[a])

