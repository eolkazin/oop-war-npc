class Npc:
    def __init__(self, nome, forca, escudo, vida, arma=None):
        self.nome = nome
        self.forca = forca
        self.escudo = escudo
        self.vida = vida
        self.arma = arma

    # mostra informações do npc
    def info(self):
        print(f"""
        == NPC INFO ==
        Nome:   {self.nome}
        Força:  {self.forca}
        Escudo: {self.escudo}
        Vida:   {self.vida}
        Arma:   {self.arma}
        """)

    # simula combate contra outro npc
    def guerra(self, inimigo):
        poder = self.forca + (self.arma or 0)
        defesa = inimigo.escudo + inimigo.vida

        if poder > defesa:
            print(f"{self.nome} venceu {inimigo.nome}")
        else:
            print(f"{self.nome} perdeu para {inimigo.nome}")


class Sniper(Npc):
    def __init__(self):
        arma = 300
        super().__init__("jonas", 200, 50, 100, arma)


class Soldad(Npc):
    def __init__(self):
        arma = 44
        super().__init__("lucas", 120, 35, 50, arma)


sniper = Sniper()
soldad = Soldad()

sniper.info()
soldad.info()

sniper.guerra(soldad)
soldad.guerra(sniper)
