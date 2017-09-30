def modul():
    n = []
    for x in range(0, 10):
        x = int(input())
        n.append(x%42)
    print(len(set(n)))#set prints the distinct values in n and len count the number of distinct values in n
modul()
