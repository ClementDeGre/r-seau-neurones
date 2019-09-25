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

