teikums = input()
saraksts = teikums.split(" ")
saraksts_zimes = []
for vards in saraksts:
    if vards[-1]==',' or vards[-1]=='.' or vards[-1]=='!' or vards[-1]=='?' or vards[-1]==':' or vards[-1]==';':
        saraksts_zimes.append(vards[-1])
saraksts_zimes.reverse()
print(saraksts_zimes)
x = saraksts.count("abc")
print(x)
for i in range(x):#darīs x reizes
    saraksts.remove("abc")
print(saraksts)