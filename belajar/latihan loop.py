sisi = 10
panjang = 1
sisi2 = 0
panjang2 = 5

    
for i in range(sisi) :
    print("*"* panjang)
    panjang += 1
    
for i in range(sisi) :
    print("*"* panjang)
    panjang -= 1 

print("\n")

n = int(input())

for i in range(n *2) :
    for j in range (n*2) :
        if i + j == n:
            print ("*", end= "")
        else :
            print (".", end="")
    print()
    
print("\n\n")

sisi = 10
panjang =1

spasi = int(sisi/2)
while True:
    if (panjang%2) :
        print(" "*spasi, "*"*panjang)
        spasi -= 1
        panjang +=1
    else :
        panjang += 1
        continue
    
    if panjang > sisi:
        break
    
for i in range (5,0,-1) :
    print(""*(5-i), end="")
    for x in range(i):
        print("*", end=" ")
    print()