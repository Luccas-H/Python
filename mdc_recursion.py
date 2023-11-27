def mdc (x,y):
    if y<= x and x%y == 0:
        print(y)
    elif x < y:
        return (mdc(y,x))
    else:
        return (mdc(y,x%y))
mdc(x = int(input(":" )), y = int(input(":" )))

