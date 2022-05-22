def nu():
    file = open("numbers.txt")
    sp = file.split(",")
    for i in sp:
        print(i)

if __name__ == '__main__':
    nu()
