print ("="*5 + "SELAMAT DATANG DI KALKULATOR SEDERHANA"+"="*5)


while True :
	angka0 = input("masukan angka pertama (atau stop)\t= "). lower()
	if angka0 == "stop" :
		print("\toke sampai jumpa")
		print("="*48)
		break

	angka1 = int(angka0)
 
	matmik = input("masuk simbol nya (+ - : x)\t\t= "). lower()
	angka2 = int(input("masukan angka kedua\t\t\t= "))

	if matmik == "+" :
		hasil = angka1 + angka2
		
	elif matmik == "-" :
		hasil = angka1 - angka2
		
	elif matmik == ":" :	
		if angka2 == 0 :
			hasil = ("error tidak bisa di bagi")
   
		elif angka1 == 0 :
			hasil = ("error tidak bisa di bagi")
   
		else :
			hasil = angka1 / angka2
	
		
	elif matmik == "x" :
		hasil = angka1 * angka2
  		
	else :
		hasil = ("simbol tidak di temukan ")
	

	print("="*48)
	print(f"\t HASILNYA ADALAH \t\t= {hasil}")
	print("="*48)