Trio = ("Messi","Neymar","Suarez",)
print(Trio)

Trio = ("Messi","Neymar","Suarez",)
print(Trio[0])

Goat = ("Ronaldo",)
print(type(Goat))

Trio = ("Messi","Neymar","Suarez",)
print(len(Trio))

# Range of Indexes
Trio = ("Messi","Neymar","Suarez",)
print(Trio[0:2])

Trio = ("Messi","Neymar","Suarez",)
print(Trio[:3])

Trio = ("Messi","Neymar","Suarez",)
print(Trio[1:])

# Python - Update Tuples
Trio = ("Messi","Neymar","Suarez",)
mnr = list(Trio)
mnr[2] = "Ronaldo"
Trio = tuple(mnr)
print(Trio)

Trio = ("Messi","Neymar","Suarez",)
mnr = list(Trio)
mnr.append ("Ronaldo")
Trio = tuple(mnr)
print(Trio)

Trio = ("Messi","Neymar","Suarez",)
mnr = list(Trio)
mnr.remove ("Suarez")
Trio = tuple(mnr)
print(Trio)

# Python - Unpack Tuples
Trio = ("Messi","Neymar","Suarez",)
(Lional, SilvaSantos, Defina) = Trio

print(Lional)
print(SilvaSantos)
print(Defina)

