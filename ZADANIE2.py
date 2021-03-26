#ZADANIE 2
import sys as system
system.stdout.write("Podaj  pierwszą liczbe: ")
a = system.stdin.readline()
system.stdout.write(a)

system.stdout.write("Podaj drugą liczbe:  ")
b = system.stdin.readline()
system.stdout.write(b)

system.stdout.write("Podaj trzecia liczbe:  ")
c = system.stdin.readline()
system.stdout.write(c)

a = int(a)
b = int(b)
c = int(c)
licz = a**b+c
print(licz)