def opener(txt):
    lis = []
    with open(txt) as txt:
        read = txt.readlines()
    for i in read:
        pos = read.index(i)
        i = i.strip("\n")
        if pos == 0 or (pos + 2) % 3 == 0:
            line = i
        else:
            line = i.rsplit(", ")
        lis.append(line)
    return lis


def text(arr):
    out = "{"
    for i in arr:
        out += i + ", "
    return out.rstrip(", ") + "}"


def dif(dif1, dif2):
    out = "{"
    for i in dif1:
        if not (i in dif2):
            out += i + ", "
    for i in dif2:
        if not (i in dif1):
            out += i + ", "
    out = out.rstrip(", ") + "}"
    print(f"Difference: Set 1 - {text(dif1)}, Set2 - {text(dif2)}, Result - {out}\n")


def inter(int1, int2):
    out = "{"
    for i in int1:
        for u in int2:
            if i == u:
                out += i + ", "
    out = out.rstrip(", ") + "}"
    print(f"Intersection: Set 1 - {text(int1)}, Set2 - {text(int2)}, Result - {out}\n")


def uni(uni1, uni2):
    out = "{"
    for i in uni1:
        if not (i in out):
            out += i + ", "
    for i in uni2:
        if not (i in out):
            out += i + ", "
    out = out.rstrip(", ") + "}"
    print(f"Union: Set 1 - {text(uni1)}, Set2 - {text(uni2)}, Result - {out}\n")


def car(car1, car2):
    out = "{"
    for i in car1:
        for u in car2:
            piece = "(" + i + ", " + u + ")"
            if not(piece in out):
                out += piece + ", "

    out = out.rstrip(", ") + "}"
    print(f"Cartesian: Set 1 - {text(car1)}, Set2 - {text(car2)}, Result - {out}\n")


def answer(item):
    size = int(item[0])
    item.pop(0)

    for i in range(0, size * 3, 3):
        if item[i] == "U":
            uni(item[i + 1], item[i + 2])
        elif item[i] == "D":
            dif(item[i + 1], item[i + 2])
        elif item[i] == "C":
            car(item[i + 1], item[i + 2])
        elif item[i] == "I":
            inter(item[i + 1], item[i + 2])
        else:
            print("Item has invalid command!\n")


answer(opener("TDE1_A.txt"))
answer(opener("TDE1_B.txt"))
answer(opener("TDE1_C.txt"))
