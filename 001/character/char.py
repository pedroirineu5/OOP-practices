class Character():

    def __init__( self, name, max_lp):
        
        if max_lp<=0:
            return ValueError
        
        self.name = name
        self.max_lp = max_lp
        self.life_points = max_lp


    def receive_dmg(self, amount_dmg):
        if amount_dmg <= 0:
            return "Nada foi feito dano negativo ou igual a zero"
       
        self.life_points -= amount_dmg

        if self.life_points <= 0:
            self.life_points = 0
            self.is_alive()

    def heal(self, amount_heal):
        if amount_heal <= 0:
            return "Nada foi feito cura negativa ou igual a zero"
        
        self.life_points += amount_heal

        if self.life_points > self.max_lp:
            self.life_points = self.max_lp

    def is_alive(self)-> bool:
        
        if self.life_points <=0:
            self.life_points = 0
            return False
        
        return True

    def exibir_status(self)->str: 
        return f"Name {self.name}, Life Points{self.life_points}/{self.max_lp}, Status: {self.is_alive()}"

    def __str__(self):
        return f"Name: {self.name}, Life Points: {self.life_points}/{self.max_lp}, Status: {self.is_alive()}"

