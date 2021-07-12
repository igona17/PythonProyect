class Jugador(object):
    def __init__(self,name,arma,vida):
        self.name=name
        self.arma=arma
        self.vida=vida


class Amigaso(Jugador):
    def __init__(self, name, arma):
        super().__init__(name, arma, vida=5)

class Enemigo(Jugador):
    def __init__(self, name, arma):
        super().__init__(name,arma,vida=5)



def getShootedByEnemigo(persona, atacante):
    persona.vida -= 1
    if persona.vida <= 0:
        print("You are dead!")
    else:
        print(f"{atacante.name} te ha disparado con un {atacante.arma}")
        print(f"En consecuencia, ahora te quedan {persona.vida} vidas")

def getShootedByAmigo(persona, atacante):
    persona.vida -= 1
    if persona.vida <= 0:
        print("You are dead!")
    else:
        print(f"{atacante.name} te ha disparado con un {atacante.arma}")
        print(f"En consecuencia, ahora te quedan {persona.vida} vidas")


obj_amigo = Amigaso("Gonzalo", "AK-47")
obj_enemigo = Enemigo("Marcelo", "Rifle")

getShootedByAmigo(obj_enemigo,obj_amigo)
getShootedByAmigo(obj_enemigo,obj_amigo)
getShootedByAmigo(obj_enemigo,obj_amigo)



