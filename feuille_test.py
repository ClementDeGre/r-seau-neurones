from reseau import Reseau

res=Reseau()

res.set_erreur(0.05)

res.print_data()
res.set_couche(4) 
res.add_all_neurones([3,5,7,3])
res.creer_reseau()
res.print_all()

res.learn([1,0,1],[1,1,0])
res.learn([1,0,0],[0,0,0])
res.learn([0,0,0],[1,0,1])
res.learn([1,1,1],[1,1,1])

res.print_all()
