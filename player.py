class Player():
    def __init__(self,name,health=100,energy=100):
        self.name = name
        self.health = health
        self.energy = energy
        print(f'Player created, Name :{self.name}')

    def attack(self,target, damage=1 ):
        self.energy -= damage
        target.health -= damage
        print(f'{self.name} Attacking to {target.name}! damage :{damage}')
        if target.is_attacked(self.name):
            self.health -= target.damage
    def show_info (self):
        print(f'{self.name} health: {self.health}')
        print(f'{self.name} energy: {self.energy}')
        if self.health <=0:
            print(f'{self.name} sudah mati')
