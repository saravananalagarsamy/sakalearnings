names  = ["ska", "mka", "lka", "ska", "mka", "lka"]


names.append("kaka")
names.remove("ska")
names.pop(2)

for name in names:
    print(name)

names.sort()

for name in names:
    print(name)

names.reverse()

for name in names:
    print(name)

names.clear()

print("List after clearing:", names)