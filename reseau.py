from fonctions import sigmoide, tangente

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
	
	def set_name(self,name):
		self.name=name

	def get_name(self):
		return self.name

	def set_erreur(self,nbr):
		if nbr>0:
			self.error=nbr

	def get_erreur(self):
		return self.error

	def set_fun_learn(self,name):
		if str.lower(name)=='tangente':
			self.fun_learn=tangente
			self.name_fun_learn='tangente'
		else:
			self.fun_learn=sigmoide
			self.name_fun_learn='sigmoide'

	def get_name_fun_learn(self):
		return self.get_name_fun_learn

	def get_data(self):
		return(self.get_name(),self.get_name_fun_learn(),self.get_erreur(),self.get_nbr_couche())

	def get_nbr_couches(self):
		return len(self.couches)

	def get_last_couche(self):
		return self.values[-1]

	def set_couche(self,value=2):
		#2 couches au min : in et out

		if self.control==0:
			if value>=2:
				for i in range(0,value):
					self.couche.append(0)
			else:
				print("il faut au moins 2 couches")
		else:
			print("le réseau est déjà créé, pas de modifs possibles")

	def add_couche(self,pos):
		if (self.control==0):
			if (pos>=0 and pos<len(self.couche)):
				self.couche.insert(pos,0)
			else:
				print("vous pouvez insérer une couche dans l'intervalle 0 - {}".format(len(self.couche)))
		else:
			print("le réseau est déjà créé, pas de modifs possibles")

	def add_neurone(self,couche,nbr=1):
		#ajouter au min 1 neurone sur la couche voulue
		if self.control==0:
			if (couche>=0 and couche<=len(self.couche)-1 and nbr>0):
				self.couche[couche]+=nbr
		else :
			print("le réseau est déjà créé, pas de modifs possibles")

	def add_all_neurones(self,tab):
		#si on veut ajouter tous les neurones
		#ex : si on veut ajouter 5 neurones à la couche 1 et 3 à la couche 2, la première val de tab sera 5 et la 2e 3
		if self.control==0:
			if len(tab)==len(self.couche):
				for i in range(0,len(tab)):
					self.add_neurone(i,tab[i])
			else :
				print("le tableau doit être de taille",len(self.couche))
		else:
			print("le réseau est déjà créé, pas de modifs possibles")