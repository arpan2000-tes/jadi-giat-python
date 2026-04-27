class hero:
	def __init__(self,name,health,attackpower,armornumber):
		self.name = name
		self.health= health
		self.attackpower= attackpower
		self.armornumber= armornumber
	
	def serang(self,lawan):
		print(self.name + 'menyerang' + lawan.name)
		lawan.diserang(self, self.attackpower)
		
	def diserang(self,lawan, attackpower_lawan):
		print(self.name + 'diserang' + lawan.name)
		attack_diterima = attackpower_lawan/self.armornumber
		print(' serangan terasa ' +str(attack_diterima))
		self.health -= attack_diterima
		print(' darah ' + self.name + 'tersisa' + str(self.health))
		
ris = hero('sniper',100,10,5)
ayam = hero('ayam',100,5,10)

ayam.serang(ris)