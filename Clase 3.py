class Jugador(object):
    def __init__(self,name,arma,vida):
        self.name=name
        self.arma=arma
        self.vida=vida

class Amigaso(Jugador):
    def __init__(self, name, arma):
        super().__init__(name, arma)

class Enemigo(Jugador):
    def __init__(self, name, arma):
        super().__init__(name,arma,vida=5)


    def Atacar(self):
        self.vida-=1
        if self.vida <= 0:
            print("You are dead!")
        else:
            print(f"te han disparado con una {self.arma}, ahora te quedan {self.vida} vidas")

obj=Enemigo("gonza","pistola")
obj.Atacar()
obj.Atacar()
obj.Atacar()
obj.Atacar()
obj.Atacar()