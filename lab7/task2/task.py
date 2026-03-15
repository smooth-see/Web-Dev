class Player:
    def __init__(self, nickname, health, weapon):
        self.nickname = nickname
        self.health = health
        self.weapon = weapon

    def shoot(self):
        return f"{self.nickname} shoots from {self.weapon}"
    
    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f"{self.nickname} died"
        return f"{self.nickname} took {damage} damage"
    
    def __str__(self):
        return f"{self.nickname} HP: {self.health} Weapon: {self.weapon}"
    

class Terrorist(Player):
    def __init__(self, nickname, health, weapon, bomb_timer):
        super().__init__(nickname, health, weapon)
        self.bomb_timer = bomb_timer

    def plant_bomb(self):
        return f"{self.nickname} planting the bomb, Timer: {self.bomb_timer}"
    
    def shoot(self):
        return f"{self.nickname} atack's with the {self.weapon} Targetting plant - A"
    
    def __str__(self):
        return f"TERRORIST: {self.nickname} HP: {self.health} Bomb: {self.bomb_timer} sec"
    
    
class CounterTerrorist(Player):
    def __init__(self, nickname, health, weapon, defuse_kit):
        super().__init__(nickname, health, weapon)
        self.defuse_kit = defuse_kit

    def defuse_bomb(self):
        if self.defuse_kit:
            time = 5
        else:
            time = 10
        return f"{self.nickname} defuses the bomb. Time: {time} sec"
    
    def shoot(self):
        return f"CT: {self.nickname} defends with {self.weapon}"
    
    def __str__(self):
        if self.defuse_kit:
              kit = " have a kit " 
        else:
            kit = " dont have a kit "
        return f"CT: {self.nickname} HP: {self.health} Kit: {kit}"


players = [
    Terrorist("s1mple", 100, "AK-47", 40),
    Terrorist("zeus", 80, "AWP", 35),
    CounterTerrorist("donk", 75, "AWP", True),
    CounterTerrorist("device", 40, "M4-A4", False),
]

print("----------PLayer's are ready-----------")
for player in players:
    print(player)

print("---------------------------------------")
for player in players:
    print(player.shoot())

print("---------------------------------------")
for player in players:
    if isinstance (player, Terrorist):
        print(player.plant_bomb())
    elif isinstance (player, CounterTerrorist):
        print(player.defuse_bomb())

print("---------------------------------------")
print(players[2].damage(10))

print(players[0].damage(30))

print(players[2].damage(15))

print(players[0].damage(70))

print(players[2].damage(100))
