# Tuple ()
# immutable , faster
names = ("sara", "mka", "lka", "sara", "mka", "lka")
for name in names:
    print(name)
print(f"sara appears {names.count("sara")} times in the tuple.")
print(f"mka at index {names.index("mka")}  in the tuple.")