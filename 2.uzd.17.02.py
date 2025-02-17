teikums = input()
vardi = teikums.split(" ") #iegūs vārdu sarakstu
for vards in vardi:# paņem vārdu no saraksta
    drukato_sk=0
    for i in range(len(vards)):
        if vards[i]>='A' and vards[i]<='Z':
            drukato_sk+=1
    print(drukato_sk)
    