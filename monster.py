class Monster():
    def __init__(self,name,health=150):
        self.health = health
        self.name = name
        self.health_init = self.health
        self.damage = 10
        print(f'Monster created, name: {self.name}')

    def is_attacked(self,attacker):
        if attacker == 'Ferry':
            self.damage = 100
            print(f'{self.name} attacking to {attacker}, damage :{self.damage}')
        else:
            print(f'{self.name} attacking to {attacker}, damage :{self.damage}')    
        return self.health < self.health_init
    def show_info (self):
        if self.health<=0:
            self.health=0
            print(f'{self.name} health: {self.health}')
            print(f'{self.name} sudah mati')
        else:
            print(f'{self.name} health: {self.health}')
