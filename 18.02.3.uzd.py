teikums = input()
vardu_nr=0
vardi = teikums.split(" ") #iegūs vārdu sarakstu
for vards in vardi:# paņem vārdu no saraksta
    drukato_sk=0
    vardu_nr+=1
    for i in range(len(vards)):
        if vards[i]>='A' and vards[i]<='Z':
            drukato_sk+=1     
    if drukato_sk==len(vards):
        print(vardu_nr)    