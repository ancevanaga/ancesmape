from math import sqrt
Ax=int(input())
Ay=int(input())
Bx=int(input())
By=int(input())
Cx=int(input())
Cy=int(input())
ab=sqrt((Ax-Bx)**2+(Ay-By)**2)
ac=sqrt((Ax-Cx)**2+(Ay-Cy)**2)
bc=sqrt((Cx-Bx)**2+(Cy-By)**2)

if ab>ac and ab>bc:
    garais=ab
    isais1=ac
    isais2=bc
elif bc>ab and bc>ac:
    garais=bc
    isais1=ab
    isais2=ac
else:
    garais=ac
    isais1=ab
    isais2=bc

if garais**2==isais1**2+isais2**2:
    print("Veido taisnleņķa trijstūri")
else:
    print("Nav")