num = input("Enter The Number : ")
x = 0
num_list = list(num)

def inc(num):
    a = int(num) + 1
    print("inc", a)
    return a

def check2(num_list):
    q = int(num_list[len(num_list)-1])

    print("check2 : ", q, "|", num)


    if q % 2 == 0:
        return 1
    else:
        return 0

def check3(num_list):

    print("check3", "|", num)
    w = 0
    while True:
        for i in range (0, len(num_list)):
            w = w + int(num_list[i])

        if w < 10000:
            if w % 3 == 0:
                return 1
            else:
                return 0
        else:
            num_list = list(str(w))

def check5(num_list):
    z = int(num_list[len(num_list)-1])
    print("check5 : ", z, "|", num)

    if z == 5 or z == 0:
        return 1
    else:
        return 0

def check7(num_list):
    pass

print(num_list)
print("Computing...")

while True:

    print("-----------------------")

    if check2(num_list) == 1:
        x += 1
        num = inc(num)
        num_list = list(str(num))
        print(num_list)

    elif check5(num_list) == 1:
        x += 1
        num = inc(num)
        num_list = list(str(num))

    elif check3(num_list) == 1:
        x += 1
        num = inc(num)
        num_list = list(str(num))

    elif check7(num_list) == 1:
        x += 1
        num = inc(num)
        num_list = list(str(num))

    else:
        break

print("-----------------------")
print("Add", x, "to the original Number")