class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.name} đã bị đánh bại"
        return None
    
    def heal(self, amount):
        self.health += amount
hero = Hero("Peter", 100)
print(hero.defend(50)) 
hero.heal(50) 
print(hero.defend(99)) 
print(hero.defend(1))  