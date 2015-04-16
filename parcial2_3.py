def superpower(x,y):
    if y==0:
        return 1
    r = x
    for n in range (y-1):
        r*=x
    return r

x=int(input("Insert number: "))
y=int(input("Insert another number: "))
print(superpower(x,y))
