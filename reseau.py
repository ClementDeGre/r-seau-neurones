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

	def get_nbr_couche(self):
		return len(self.couche)

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

	def creer_reseau(self):
		#on initialise toutes les connexions entre neurones
		# Les poids sont mis à 0.5 par def
		#on initialise aussi le tableau des valeurs des neurones à 0

		test =0
		for j in range(0,len(self.couche)):
			if self.couche[j]<=0:
				print("la couche",j,"doit contenir au moins 1 neurone")
				test=1
		if test!=1:
			if self.control==0:
				self.control=1
				for i in range(0,len(self.couche)): #boucle sur les couches
					add=[]
					add1=[]
					add_values=[]
					for j in range(0,self.couche[i]): #boucle sur les neurones de la couche i
						if i!=len(self.couche)-1: #pas créer de liens à la dernière couche
							for k in range(0,self.couche[i+1]):
								add1.append(0.5)
							add.append(add1)
							add1=[]
						add_values.append(0)
					if i!=len(self.couche)-1:
						self.link.append(add) #tableau de tableau
					self.values.append(add_values)
			else:
				print("le réseau initialisé")
		else :
			print("vous ne pouvez pas lancer l'initialisation")

	def parcourir(self,tab):
		#algo de propagation
		#param = données à tester
		if self.control==1:
			if len(tab)==self.couche[0]:  #vérfi que autant d'entrée que le nb de neurone dans couche d'entrée
				for i in range(0,len(tab)):
					#on stocke dans la première couche les données d'entrée
					self.values[0][i]=tab[i]
				for i in range(1,len(self.values)):  #boucle sur les couches (pas sûr)
					for j in range(0,len(self.values[i])): #boucle sur les neurones de la couche i
						var=0
						for k in range(0,len(self.values[i-1])): #boucle sur les neurones de la couche précédente
							#on stocke la somme pondérée dans le prochain neurone
							var+=self.values[i-1][k]*self.link[i-1][k][j]
						self.values[i][j]=self.fun_learn(var)
			else:
				print("la couche d'entrée doit contenir", self.couche[0]," valeurs")
		else:
			print("Réseau non initialisé")

	def retropropagation(self,tab):
		#prend en param les données attendues (apprentissage supervisé)

		if len(tab)==len(self.values[len(self.values)-1]):
			for i in range(0,len(tab)): #boucle sur nb de neurone de sortie
				#on stocke dans la dernière couche la soustraction (valeur voulue-valeur trouvée)
				self.values[len(self.values)-1][i]=tab[i] - self.values[len(self.values)-1][i]
			for i in range(len(self.values)-1,0,-1): #boucle sur les couches, de la fin au début
				for j in range(0,len(self.values[i-1])):
					for k in range(0,len(self.link[i-1][j])):
						somme=0
						for l in range(0,len(self.values[i-1])):
							#on effectue la somme pondérée du neurone vers lequel pointe la connexion
							somme+=self.values[i-1][l]*self.link[i-1][l][k]
						somme=self.fun_learn(somme)
						#mise à jour du poids de la connexion
						self.link[i-1][j][k]-=self.get_erreur()*(-1*self.values[i][k]*somme*(1-somme)*self.values[i-1][j])
				for j in range(0,len(self.values[i-1])):
					somme = 0
					for k in range(0,len(self.values[i])):
						#on met à jour les neurones de la prochaine couche en fonction de l'erreur qui se rétropropage
						somme+=self.values[i][k]*self.link[i-1][j][k]
					self.values[i-1][j]=somme

	def learn(self,entree,sortie):
		#premier param est l'ensemble de valeurs à tester
		#le deuxième est le résultat attendu

		if self.control==1:
			if len(entree)==self.couche[0] and len(sortie)==self.couche[len(self.couche)-1]:
				self.parcourir(entree)
				self.retropropagation(sortie)
			else:
				print("la couche d'entrée doit contenir", self.couche[0], " valeurs")
				print("la couche de sortie doit contenir",self.couche[len(self.couche)-1], " valeurs")

	def print_last_couche(self):
		print(self.values[len(self.values)-1])

	def print_data(self):
		tab = self.get_data()
		print("Nom du reseau :", tab[0],"\nFonction d'apprentissage :", tab[1],"\nValeur d'erreur d'apprentissage :", tab[2],"\nNombre de couche dans le réseau :", tab[3])


	def print_all(self):
		print('Values :')
		self.print_values()
		print('\nLink :')
		self.print_link()

	def print_values(self):
		i = 1
		for each in self.values:
			print("Couche ",i,":")
			i+=1
			print(each)

	def print_link(self):
		i = 1
		for each in self.link:
			print("Liens ",i,":")
			i+=1
			for k in each:
				print (k)
			print()
    
	def print_couche(self):
		print (self.couche)