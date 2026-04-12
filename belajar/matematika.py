print ("="*5 + "SELAMAT DATANG DI KALKULATOR SEDERHANA"+"="*5)
angka1 = int(input("masukan angka pertama\t\t= "))
matmik = input("masuk simbol nya (+ - : x)\t= "). lower()
angka2 = int(input("masukan angka kedua\t\t= "))

if matmik == "+" :
	hasil = angka1 + angka2
	
elif matmik == "-" :
	hasil = angka1 - angka2
	
elif matmik == ":" :
	hasil = angka1 / angka2
	
elif matmik == "x" :
	hasil = angka1 * angka2
	
else :
	hasil = ("simbol tidak di temukan ")

print("="*48)
print(f"\t HASILNYA ADALAH \t= {hasil}")
print("="*48)