class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

class Player(Character):
    def __init__(self, name):
        # 勇者の初期ステータスは例示です
        super().__init__(name, hp=100, attack=20, defense=10)