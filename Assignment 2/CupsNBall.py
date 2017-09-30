def cupsnball ():
    inp = input()
    a = 1
    b = 0
    c = 0
    for x in inp:
        if x == "A":
            a, b = b, a #swap the contents of a and b
        elif x == "B":
            b, c = c, b #swap the contents of b and c
        elif x == "C":
            a, c = c, a #swap the contents of a and c
    if a == 1:
        print(1)
    elif b == 1:
        print(2)
    elif c == 1:
        print(3)
cupsnball()
