
podejrzane = [1,-3,-2,2]

def zwroc(x):
    y =2*x**3 + 3*x**2 - 12*x+ 5 #tu wpisz funkcje
    print("Dla x= ",x,"zwraca :",y)
    return y

# zwroc(-2)
# zwroc(1)

for i in podejrzane:
    zwroc(i)