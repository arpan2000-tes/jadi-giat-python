class Karakter:
    def __init__(self, nama, hp, attack):
        self.nama = nama
        self.hp = hp
        self.attack = attack

    def terima_damage(self, damage):
        """
        Method ini bertugas mengurangi 'self.hp' 
        sesuai dengan jumlah 'damage' yang diterima.
        """
        self.hp -= damage
        
        
        # Baris ini akan mencetak status setelah damage diterima
        print(f"{self.nama} menerima {damage} damage! HP tersisa: {self.hp}")

    def serang(self, target):
        """
        Method ini membuat karakter ini menyerang karakter lain (target).
        """
        print(f"\n{self.nama} melancarkan serangan ke {target.nama}!")
        
        # TODO: Panggil method terima_damage() milik objek 'target'.
        # Gunakan 'self.attack' sebagai nilai damage yang dimasukkan ke dalam kurung ().
        target.terima_damage(self.attack)
        
        

# --- Bagian Pengujian Program ---

# 1. Buat dua objek karakter
karakter1 = Karakter("Elysia", 1500, 300)
musuh = Karakter("Honkai Beast", 2000, 150)

# Menampilkan status awal
print(f"=== STATUS AWAL ===")
print(f"{karakter1.nama} [HP: {karakter1.hp}] vs {musuh.nama} [HP: {musuh.hp}]")

# 2. Karakter 1 menyerang musuh
# TODO: Panggil method serang() dari 'karakter1' dan masukkan 'musuh' sebagai targetnya
karakter1.serang(musuh)


# 3. Musuh menyerang balik Karakter 1
# TODO: Panggil method serang() dari 'musuh' dan masukkan 'karakter1' sebagai targetnya
musuh.serang(karakter1)




class Hypercar:
    def __init__(self, model, top_speed):
        self.model = model
        self.top_speed = top_speed
        self.kecepatan = 0  # Mobil selalu mulai dari posisi diam (0 km/jam)

    def gas(self, nilai_akselerasi):
        """
        Menambah kecepatan mobil. Kecepatan akhir tidak boleh melebihi 'top_speed'.
        """
        self.kecepatan += nilai_akselerasi
        
        # TODO: Buat logika IF di bawah ini.
        # Jika self.kecepatan lebih besar (>) dari self.top_speed,
        # maka atur (paksakan) self.kecepatan agar nilainya sama dengan self.top_speed.
        if self.kecepatan > self.top_speed:
            self.kecepatan = self.top_speed
        
        
        print(f"GAS! {self.model} melaju di kecepatan {self.kecepatan} km/jam")

    def rem(self, nilai_pengereman):
        """
        Mengurangi kecepatan mobil. Kecepatan akhir tidak boleh di bawah 0.
        """
        # TODO 1: Kurangi self.kecepatan dengan nilai_pengereman (Gunakan -=)
        self.kecepatan -= nilai_pengereman
        
        # TODO 2: Buat logika IF. 
        # Jika self.kecepatan kurang dari (<) 0, 
        # maka atur self.kecepatan menjadi 0.
        if self.kecepatan < 0:
            self.kecepatan = 0
        
        print(f"REM! Kecepatan {self.model} turun menjadi {self.kecepatan} km/jam")

# --- Bagian Pengujian Program ---

utopia = Hypercar("Pagani Utopia", 352)
huayra = Hypercar("Pagani Huayra", 383)

print("=== SIMULASI HYPERCAR ===")

# 1. Utopia ngegas dengan akselerasi 150
# TODO: Panggil method gas() dari objek 'utopia' dengan memasukkan nilai 150
utopia.gas(150)

# 2. Huayra langsung ngegas pol 400 (ini melebihi top speed-nya yang hanya 383!)
# TODO: Panggil method gas() dari objek 'huayra' dengan memasukkan nilai 400
huayra.gas(400)

# 3. Utopia ngerem mendadak dengan kekuatan 200 (harusnya mentok di 0, tidak jadi minus)
# TODO: Panggil method rem() dari objek 'utopia' dengan memasukkan nilai 200
utopia.rem(200)