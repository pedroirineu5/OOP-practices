class Character():

    def __init__( self, name, life_points):
        
        self.name = name
        self.life_points = life_points

    def receive_dmg(self, amount_dmg):
        if amount_dmg <= 0:
            return "Nada foi feito dano negativo ou igual a zero"
        
        self.life_points -= amount_dmg

    def heal(self, amount_heal):
        if amount_heal <= 0:
            return "Nada foi feito cura negativa ou igual a zero"
        
        self.life_points += amount_heal

    def is_alive(self)-> bool:
        
        if self.life_points <=0:
            return False
        
        return True

    def __str__(self):
        return f"Name: {self.name}, MAX_HP: {self.life_points}, Status: {self.is_alive()}"
