class Amigaso(object):
    def __init__(self, ami_name, arma):
        self.ami_name = ami_name
        self.arma = arma

class Enemigo(Amigaso):
    def __init__(self, ami_name, arma, enem_name, lugar, vida):
        super(Enemigo,self).__init__(ami_name,arma)
        self.enem_name = enem_name
        self.lugar = lugar
        self.vida = vida

    def Disparar(self):
        self.vida-=1
        if self.vida <= 0:
            print("You are dead!")
        else:
            print(f"{self.ami_name} te ha disparado con un {self.arma} mientras estabas en {self.lugar}")
            print(f"En consecuencia, ahora te quedan {self.vida}")

obj2=Enemigo("Juan", "Ak-47", "Pedro", "la playa", 5)
obj2.Disparar()
obj2.Disparar()
obj2.Disparar()
obj2.Disparar()
obj2.Disparar()
obj2.Disparar()