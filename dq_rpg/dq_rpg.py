import random
import sys

# キャラクターの基本クラス
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

# プレイヤークラス（勇者）
class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=20, defense=10)
        self.exp = 0
        self.level = 1

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name}は{amount}の経験値を獲得！ (累計: {self.exp})")
        # レベルアップの閾値: 現在のレベル×50
        if self.exp >= self.level * 50:
            self.level += 1
            self.exp = 0
            self.max_hp += 20
            self.hp = self.max_hp
            self.attack += 5
            self.defense += 3
            print(f"{self.name}はレベルアップ！ 現在のレベル: {self.level}")

# 敵クラス（プレイヤーと同じ基本機能を使用）
class Enemy(Character):
    pass

def battle(player, enemy):
    print("\n戦闘開始！")
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}のHP: {player.hp}/{player.max_hp}")
        print(f"{enemy.name}のHP: {enemy.hp}/{enemy.max_hp}")
        print("1: 攻撃する  2: 逃げる")
        choice = input("行動を選んでください: ")
        if choice == "1":
            damage = max(0, player.attack - enemy.defense + random.randint(-2, 2))
            enemy.take_damage(damage)
            print(f"{player.name}の攻撃！ {enemy.name}に {damage} のダメージ！")
        elif choice == "2":
            if random.random() < 0.5:
                print("逃げ切った！ バトル終了。")
                return False
            else:
                print("逃げられなかった！")
        else:
            print("無効な選択です。")
            continue

        if enemy.is_alive():
            damage = max(0, enemy.attack - player.defense + random.randint(-2, 2))
            player.take_damage(damage)
            print(f"{enemy.name}の攻撃！ {player.name}に {damage} のダメージ！")

    if player.is_alive():
        print(f"\n{player.name}の勝利！")
        player.gain_exp(50)
        return True
    else:
        print(f"\n{player.name}は倒れた...")
        return False

def main():
    print("ドラゴンクエスト風RPGへようこそ！")
    name = input("あなたの勇者の名前を入力してください: ")
    player = Player(name)

    while True:
        # 敵は毎回新規生成（例: スライム）
        enemy = Enemy("スライム", hp=50, attack=15, defense=5)
        result = battle(player, enemy)
        if not player.is_alive():
            break
        choice = input("もう一度戦いますか？ (Y/N): ")
        if choice.lower() != "y":
            break
    print("ゲーム終了。ありがとうございました！")
    sys.exit()

if __name__ == "__main__":
    main()



# 既存のEnemyクラスはそのまま使うので、テンプレートを定義
enemy_templates = [
    {"name": "スライム",   "hp": 50,  "attack": 15, "defense": 5},
    {"name": "ゴブリン",   "hp": 60,  "attack": 18, "defense": 7},
    {"name": "オーク",     "hp": 80,  "attack": 20, "defense": 10},
    {"name": "バット",     "hp": 40,  "attack": 12, "defense": 4},
    {"name": "ウルフ",     "hp": 70,  "attack": 17, "defense": 8},
    {"name": "スケルトン", "hp": 55,  "attack": 16, "defense": 6},
    {"name": "ゾンビ",     "hp": 65,  "attack": 14, "defense": 9},
    {"name": "ドラゴン",   "hp": 120, "attack": 25, "defense": 15},
    {"name": "ダークナイト", "hp": 90, "attack": 22, "defense": 12},
    {"name": "魔法使い",   "hp": 45,  "attack": 30, "defense": 3}
]

def choose_enemy():
    # enemy_templates からランダムに1体選ぶ
    template = random.choice(enemy_templates)
    return Enemy(template["name"], hp=template["hp"], attack=template["attack"], defense=template["defense"])