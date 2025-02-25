teikums = input()
saraksts = teikums.split()
pedejais = saraksts[-1]
saraksts.insert(2, "Sveiks!")
saraksts.sort(reverse=True)
print(saraksts)
print(saraksts.index("Sveiks!"))
if "abc" in saraksts:
    print("JA")
else:
    print("NE")
if saraksts[-1]==saraksts[3]:
    print("JA")
else:
    print("NE")

