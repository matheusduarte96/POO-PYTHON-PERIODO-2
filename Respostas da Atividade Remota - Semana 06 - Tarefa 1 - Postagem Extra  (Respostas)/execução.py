from classes import ControleRemoto, televisao

c1 = ControleRemoto(True)
Tv1 = televisao(True, 6, 15)
c1.LigarDesligar()
c1.vincularTv(Tv1)
c1.ligarTv()

print("-="*15)

c2 = ControleRemoto(True)
Tv2 = televisao(True, 18, 45)
c2.LigarDesligar()
c2.vincularTv(Tv2)
c2.ligarTv()

print("-="*15)

c3 = ControleRemoto(True)
Tv3 = televisao(True, 18, 45)
c3.LigarDesligar()
c3.desvincularTv()
c3.ligarTv()
