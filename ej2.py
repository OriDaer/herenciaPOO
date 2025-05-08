class Mago:# Defino clases base
    def hechizos(self):
        print("El mago lanza un hechizo.")
class Guerrero:
    def defensa(self):
        print("El guerrero se defiende con su escudo.")
class Elfo:
    def aura(self):
        print("El elfo emana un aura mágica.")
print("=== Herencia: Guerrero, Elfo, Mago ===")# DarkLord hereda de Guerrero y Elfo
class DarkLord1(Guerrero, Elfo, Mago):
    pass
oscuro1 = DarkLord1()
oscuro1.defensa()
oscuro1.aura()
oscuro1.hechizos()
print("MRO:", DarkLord1.__mro__)
print()
print("=== Herencia: Elfo, Guerrero, Mago ===")# DarkLord hereda de Elfo y Guerrero
class DarkLord2(Elfo, Guerrero, Mago):
    pass
oscuro2 = DarkLord2()
oscuro2.defensa()
oscuro2.aura()
oscuro2.hechizos()
print("MRO:", DarkLord2.__mro__)
