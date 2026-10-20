class Character():

    def __init__( self, name, life_points, mana_points, status: bool):
        self.name = name
        self.life_points = life_points
        self.mana_points = mana_points
        self.status = status

    def __str__(self):
        return f"Name: {self.name}, MAX_HP: {self.life_points}, Status: {self.status}"
        pass