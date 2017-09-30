def kmp ():
    inp = input() #input something
    result = ""
    for x in inp.upper().split("-"):
        result += x[0] #this adds the result of the loop to the empty string(result) above
    print(result)
kmp()
