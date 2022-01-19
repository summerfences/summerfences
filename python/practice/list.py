fart = [1, "two", 2.999, True, "5"]

fart.append("six")
print(fart)
fart.remove(1)
print(fart)
fart.insert(2, 3)
print(fart)

# print a range, last is max NOT included
print(fart[0:3])

# alternative way to remove
del(fart[0:3])
print(fart)
