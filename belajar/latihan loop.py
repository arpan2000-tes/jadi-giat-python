sisi = 5
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
