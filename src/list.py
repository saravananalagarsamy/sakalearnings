# This is a sample Python script demonstrating list operations.
# mutable, most flexible
names  = ["ska", "mka", "lka", "ska", "mka", "lka"]


names.append("kaka")
names.remove("ska")
names.pop(3)

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