teikums = input()
ir_drukats=False
for i in range(len(teikums) ):
    if teikums[i]>='A' and teikums[i]<='Z':
        print("IR DRUKĀTAIS")
        ir_drukats=True
        break
if ir_drukats==False:
    print("NAV DRUKĀTAIS")
