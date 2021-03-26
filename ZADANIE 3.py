#ZADANIE 3
a = input("Wczytaj pierwsza liczbe: ")
b = input("Wczytaj druga liczbe: ")
c = input("Wczytaj trzecia liczbe: ")
a = int(a)
b = int(b)
c = int(c)
if a>b:
    print("liczba" +str(a) + "jest większa")
elif c>a:
    print("liczba" + str(c) + "jest większa")
elif c<b:
     print("liczba" + str(b) + "jest większa")
elif a<b:
    print("liczba " + str(b) + " jest większa")
else:
    print("wprowadzone liczby są równe")