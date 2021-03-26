#ZADANIE 5
x = 0
parzyste = []
while x != 10:
     liczba = input("Wprowadz liczbe: ")
     liczba = float(liczba)
     if liczba % 2 == 0:
         parzyste.append(liczba)
     x += 1
print(parzyste)