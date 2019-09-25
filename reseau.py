class Reseau:
	def __init__(self,name='Unknown',learn='sigmoide',error=0.001):
		#nom, fonction d'activation et erreur
		self.name=name
		if 'tangente'==str.lower(learn):
			self.fun_learn=tangente
			self.name_fun_learn='tangente'
		else:
			self.fun_learn=sigmoide
			self.name_fun_learn='sigmoide'
		self.error=error
		self.couche=[] #nb de neurones par couches
		self.link=[] #le tableau avec tous les poids
		self.values=[] #le tableau avec valeurs des neurones

		self.control=0 #controleur pour empecher ajout de couches/neurones après premier lancement
print('ok')